import json
from django.db.models import OuterRef, Exists, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.contrib import messages
from .models import (
    StudyMaterial, FlashcardSet, Flashcard,
    Quiz, QuizQuestion, QuizAnswer, Upvote, Comment, Report, SavedMaterial
)
from modules.models import StudentModule, Module, PinnedModule


@login_required
def filter_materials(request):
    materials = StudyMaterial.objects.filter(
        is_published=True,
        is_deleted=False,
        is_hidden_by_admin=False
    )

    material_type = request.GET.get('type')
    module_id = request.GET.get('module')

    if material_type:
        materials = materials.filter(material_type=material_type)

    if module_id:
        materials = materials.filter(module_id=module_id)

    materials = materials.order_by('-created_at')

    data = []
    for mat in materials:
        data.append({
            'id': mat.id,
            'title': mat.title,
            'type': mat.get_material_type_display(),
            'module_id': mat.module_id if mat.module else 'Private',
            'created_at': mat.created_at.strftime('%Y-%m-%d %H:%M'),
        })

    return JsonResponse({
        'total_count': materials.count(),
        'results': data
    })


@login_required
def browse_materials(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    materials = StudyMaterial.objects.filter(
        is_deleted=False, is_published=True, is_hidden_by_admin=False, module_id=module_id
    ).select_related('module', 'owner__user')

    student = None
    is_subscribed = False
    is_favourited = False
    saved_material_ids = []

    if request.user.is_authenticated and request.user.role == 'student':
        student = request.user.student_profile
        is_subscribed = StudentModule.objects.filter(student=student, module=module).exists()
        is_favourited = PinnedModule.objects.filter(student=student, module=module).exists()
        saved_material_ids = list(SavedMaterial.objects.filter(
            student=student,
            study_material__module=module
        ).values_list('study_material_id', flat=True))

    materials = materials.annotate(
        upvote_count=Count('upvotes', distinct=True),
        comment_count=Count('comments', distinct=True),
    )

    return render(request, 'modules/module_detail.html', {
        'module': module,
        'materials': materials,
        'is_subscribed': is_subscribed,
        'is_favourited': is_favourited,
        'saved_material_ids': saved_material_ids,
        'student': student,
    })


@login_required
def my_resources(request):
    if request.user.role != 'student':
        return render(request, 'materials/my_resources.html', {'error': 'Only students can view their resources'})

    student = request.user.student_profile

    active_subscriptions = StudentModule.objects.filter(student=student, is_hidden_by_student=False).select_related(
        'module')
    archived_subscriptions = StudentModule.objects.filter(student=student, is_hidden_by_student=True).select_related(
        'module')

    saved_materials = SavedMaterial.objects.filter(student=student)

    created_mats = student.created_materials.filter(is_deleted=False)
    saved_mats = StudyMaterial.objects.filter(
        id__in=saved_materials.values_list('study_material_id', flat=True),
        is_deleted=False,
        is_published=True
    )

    all_materials = (created_mats | saved_mats).distinct().select_related('module', 'owner__user')

    all_materials = all_materials.annotate(
        user_has_saved=Exists(
            SavedMaterial.objects.filter(student=student, study_material=OuterRef('pk'))
        ),
        is_own_material=Exists(
            student.created_materials.filter(id=OuterRef('pk'))
        )
    )

    modules_with_materials = []
    for subscription in active_subscriptions:
        module = subscription.module
        module_materials = all_materials.filter(module=module).order_by('-created_at')
        if module_materials.exists():
            modules_with_materials.append({
                'module': module,
                'materials': module_materials,
                'material_count': module_materials.count(),
            })

    archived_modules_with_materials = []
    for subscription in archived_subscriptions:
        module = subscription.module
        module_materials = all_materials.filter(module=module).order_by('-created_at')
        if module_materials.exists():
            archived_modules_with_materials.append({
                'module': module,
                'materials': module_materials,
                'material_count': module_materials.count(),
            })

    private_materials = created_mats.filter(module__isnull=True).order_by('-created_at')

    context = {
        'modules_with_materials': modules_with_materials,
        'archived_modules_with_materials': archived_modules_with_materials,
        'private_materials': private_materials,
        'total_materials': all_materials.count(),
        'subscription_count': active_subscriptions.count(),
        'archived_count': archived_subscriptions.count(),
    }

    return render(request, 'materials/my_resources.html', context)
@login_required
@require_http_methods(["POST"])
def create_flashcard_set(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        module_id = data.get('module_id')
        is_published = data.get('is_published', False)
        cards_data = data.get('cards', [])

        if not module_id:
            is_published = False

        if not title or not cards_data:
            return JsonResponse({"error": "Missing title or cards data"}, status=400)

        student = request.user.student_profile

        with transaction.atomic():
            material = StudyMaterial.objects.create(
                title=title,
                material_type='flashcard',
                owner=student,
                module_id=module_id if module_id else None,
                is_published=is_published
            )

            flashcard_set = FlashcardSet.objects.create(study_material=material)

            flashcards_to_create = []
            for index, card in enumerate(cards_data):
                flashcards_to_create.append(
                    Flashcard(
                        flashcard_set=flashcard_set,
                        front=card.get('front', ''),
                        back=card.get('back', ''),
                        order=card.get('order', index + 1)
                    )
                )
            Flashcard.objects.bulk_create(flashcards_to_create)

        return JsonResponse({
            "message": "Flashcard set created successfully",
            "material_id": material.pk,
            "cards_count": len(flashcards_to_create)
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
@require_http_methods(["POST"])
def create_quiz(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        module_id = data.get('module_id')
        is_published = data.get('is_published', False)
        questions_data = data.get('questions', [])

        if not module_id:
            is_published = False

        if not title or not questions_data:
            return JsonResponse({"error": "Missing title or questions data"}, status=400)

        student = request.user.student_profile

        with transaction.atomic():
            material = StudyMaterial.objects.create(
                title=title,
                material_type='quiz',
                owner=student,
                module_id=module_id if module_id else None,
                is_published=is_published
            )

            quiz = Quiz.objects.create(study_material=material)

            for q_index, q_data in enumerate(questions_data):
                question = QuizQuestion.objects.create(
                    quiz=quiz,
                    question_text=q_data.get('question_text', ''),
                    question_type=q_data.get('question_type', 'single'),
                    order=q_data.get('order', q_index + 1)
                )

                answers_data = q_data.get('answers', [])
                answers_to_create = []
                for a_index, a_data in enumerate(answers_data):
                    answers_to_create.append(
                        QuizAnswer(
                            question=question,
                            answer_text=a_data.get('answer_text', ''),
                            is_correct=a_data.get('is_correct', False),
                            order=a_data.get('order', a_index + 1)
                        )
                    )
                QuizAnswer.objects.bulk_create(answers_to_create)

        return JsonResponse({
            "message": "Quiz created successfully",
            "material_id": material.pk,
            "questions_count": len(questions_data)
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def create_flashcard_page(request, module_id=None):
    student = request.user.student_profile
    subscribed_modules = StudentModule.objects.filter(student=student).select_related('module').order_by(
        'module__school__name', 'module__id')
    context = {
        'subscribed': [sm.module for sm in subscribed_modules],
        'initial_module_id': module_id,
    }
    return render(request, 'materials/create_flashcard.html', context)


@login_required
def create_quiz_page(request, module_id=None):
    student = request.user.student_profile
    subscribed_modules = StudentModule.objects.filter(student=student).select_related('module').order_by(
        'module__school__name', 'module__id')
    context = {
        'subscribed': [sm.module for sm in subscribed_modules],
        'initial_module_id': module_id,
    }
    return render(request, 'materials/create_quiz.html', context)


def _get_interaction_data(request, material):
    upvote_count = material.upvotes.count()
    user_has_upvoted = False
    comments = []

    if request.user.is_authenticated and request.user.role == 'student':
        student = request.user.student_profile
        user_has_upvoted = material.upvotes.filter(student=student).exists()
        comments = material.comments.filter(is_deleted=False).select_related('student__user').order_by('-created_at')

    return upvote_count, user_has_upvoted, comments


@login_required
def view_flashcard(request, material_id):
    material = get_object_or_404(StudyMaterial, id=material_id, material_type='flashcard')

    if material.owner != request.user.student_profile and not material.is_published:
        return render(request, 'materials/my_resources.html',
                      {'error': 'You do not have permission to view this material'})

    flashcard_set = material.flashcard_set
    flashcards = flashcard_set.cards.all().order_by('order')

    upvote_count, user_has_upvoted, comments = _get_interaction_data(request, material)

    context = {
        'flashcard_set': flashcard_set,
        'flashcards': flashcards,
        'upvote_count': upvote_count,
        'user_has_upvoted': user_has_upvoted,
        'comments': comments,
    }

    return render(request, 'materials/view_flashcard.html', context)


@login_required
def view_quiz(request, material_id):
    material = get_object_or_404(StudyMaterial, id=material_id, material_type='quiz')

    if material.owner != request.user.student_profile and not material.is_published:
        return render(request, 'materials/my_resources.html',
                      {'error': 'You do not have permission to view this material'})

    quiz = material.quiz
    questions = quiz.questions.all().order_by('order')

    upvote_count, user_has_upvoted, comments = _get_interaction_data(request, material)

    context = {
        'quiz': quiz,
        'questions': questions,
        'upvote_count': upvote_count,
        'user_has_upvoted': user_has_upvoted,
        'comments': comments,
    }

    return render(request, 'materials/view_quiz.html', context)


@login_required
def toggle_upvote(request, material_id):
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can upvote'}, status=403)

    material = get_object_or_404(StudyMaterial, id=material_id, is_published=True)
    student = request.user.student_profile

    upvote, created = Upvote.objects.get_or_create(student=student, study_material=material)
    if not created:
        upvote.delete()

    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def add_comment(request, material_id):
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can comment'}, status=403)

    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    material = get_object_or_404(StudyMaterial, id=material_id, is_published=True)
    student = request.user.student_profile

    if not student.can_comment:
        messages.error(request, 'You have been restricted from commenting.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    content = request.POST.get('content', '').strip()
    if content:
        Comment.objects.create(student=student, study_material=material, content=content)

    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    student = request.user.student_profile

    if comment.student != student and request.user.role != 'moderator' and not request.user.is_superuser:
        messages.error(request, 'You cannot delete this comment.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    comment.is_deleted = True
    comment.save()
    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def toggle_publish_material(request, material_id):
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can manage materials'}, status=403)

    student = request.user.student_profile
    material = get_object_or_404(StudyMaterial, id=material_id, owner=student)

    if material.module is None:
        messages.error(request, 'Personal resources cannot be published. Assign to a module first.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    material.is_published = not material.is_published
    material.save()

    if material.is_published:
        messages.success(request, f'"{material.title}" is now published.')
    else:
        messages.success(request, f'"{material.title}" is now private.')

    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
@require_http_methods(["POST"])
def delete_material(request, material_id):
    if request.user.role != 'student':
        messages.error(request, 'Only students can delete materials.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    student = request.user.student_profile
    material = get_object_or_404(StudyMaterial, id=material_id, owner=student)

    material.is_deleted = True
    material.save()

    messages.success(request, f'"{material.title}" has been deleted.')
    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def report_material(request, material_id):
    if request.user.role != 'student':
        messages.error(request, 'Only students can report materials.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    material = get_object_or_404(StudyMaterial, id=material_id)
    student = request.user.student_profile

    if Report.objects.filter(reporter=student, study_material=material, comment__isnull=True).exists():
        messages.error(request, 'You have already reported this material.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    reason = request.POST.get('reason', 'other')
    details = request.POST.get('details', '').strip()

    Report.objects.create(
        reporter=student,
        study_material=material,
        reason=reason,
        details=details,
    )

    messages.success(request, 'Report submitted. A moderator will review it.')
    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def report_comment(request, comment_id):
    if request.user.role != 'student':
        messages.error(request, 'Only students can report comments.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    comment = get_object_or_404(Comment, id=comment_id)
    student = request.user.student_profile

    if Report.objects.filter(reporter=student, comment=comment).exists():
        messages.error(request, 'You have already reported this comment.')
        return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))

    reason = request.POST.get('reason', 'other')
    details = request.POST.get('details', '').strip()

    Report.objects.create(
        reporter=student,
        study_material=comment.study_material,
        comment=comment,
        reason=reason,
        details=details,
    )

    messages.success(request, 'Comment reported. A moderator will review it.')
    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))


@login_required
def toggle_save_material(request, material_id):
    material = get_object_or_404(StudyMaterial, id=material_id, is_published=True)
    student = request.user.student_profile

    if material.owner == student:
        messages.error(request, "You cannot save your own material.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    saved_item, created = SavedMaterial.objects.get_or_create(
        student=student,
        study_material=material
    )

    if not created:
        saved_item.delete()
        messages.success(request, f'"{material.title}" removed from My Resources.')
    else:
        messages.success(request, f'"{material.title}" saved to My Resources.')

    return redirect(request.META.get('HTTP_REFERER', '/'))