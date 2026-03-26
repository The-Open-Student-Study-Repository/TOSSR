import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db import transaction
from .models import (
    StudyMaterial, FlashcardSet, Flashcard,
    Quiz, QuizQuestion, QuizAnswer
)
from modules.models import StudentModule, Module, PinnedModule


def filter_materials(request):

    """
        FRONTEND DEVELOPER INSTRUCTIONS (AJAX Filtering API)
        —————————————————————————————————————————————————————————————————————————
        This is the API endpoint for the "Funnel" filtering tool on the materials page.
        As per the WAD2 rubric, please use JavaScript/JQuery/AJAX to fetch data from this endpoint.

        ENDPOINT:
        {% url 'filter_materials' %} (Resolves to /materials/filter/)

        HTTP METHOD:
        GET

        ACCEPTED URL PARAMETERS (Both are optional):
        - type: (String) 'flashcard' or 'quiz'
        - module: (String) The 16-character module ID (e.g., 'COMP1001')

        RESPONSE FORMAT (JSON):
        {
            "total_count": 5,
            "results": [
                {
                    "id": 1,
                    "title": "Material Title",
                    "type": "Quiz",
                    "module_id": "COMP1001",
                    "created_at": "YYYY-MM-DD HH:MM"
                },
                // ... other items
            ]
        }

        USAGE HINT:
        Trigger an AJAX GET request to this URL when the user interacts with the filter UI.
        Pass the selected values as query parameters. Upon a successful response, clear the
        current materials list in the DOM and dynamically iterate over `response.results`
        to render the updated items.
        —————————————————————————————————————————————————————————————————————————
        """

    # Only show published, non-deleted, and non-hidden materials
    materials = StudyMaterial.objects.filter(
        is_published=True,
        is_deleted=False,
        is_hidden_by_admin=False
    )

    # Get filtering parameters from the AJAX GET request
    material_type = request.GET.get('type')
    module_id = request.GET.get('module')

    # Apply the filters dynamically if the parameters are provided
    if material_type:
        materials = materials.filter(material_type=material_type)

    if module_id:
        materials = materials.filter(module_id=module_id)

    # Order the results by newest first
    materials = materials.order_by('-created_at')

    # Serialize the QuerySet into a list of dictionaries for JSON response
    data = []
    for mat in materials:
        data.append({
            'id': mat.id,
            'title': mat.title,
            # get_material_type_display() converts 'flashcard' to 'Flashcard'
            'type': mat.get_material_type_display(),
            'module_id': mat.module_id if mat.module else 'Private',
            'created_at': mat.created_at.strftime('%Y-%m-%d %H:%M'),
        })

    # Return the JSON response
    return JsonResponse({
        'total_count': materials.count(),
        'results': data
    })


@login_required()
def browse_materials(request, module_id):
    module = Module.objects.get(id=module_id)
    materials = StudyMaterial.objects.filter(
        is_deleted=False, is_published=True, is_hidden_by_admin=False, module_id=module_id
    ).select_related('module')

    is_subscribed = False
    is_favourited = False
    if request.user.is_authenticated and request.user.role == 'student':
        student = request.user.student_profile
        is_subscribed = StudentModule.objects.filter(student=student, module=module).exists()
        is_favourited = PinnedModule.objects.filter(student=student, module=module).exists()

    return render(request, 'modules/module_detail.html', {
        'module': module,
        'materials': materials,
        'is_subscribed': is_subscribed,
        'is_favourited': is_favourited,
    })

@login_required
def my_resources(request):
    """Display all resources (materials) created by the logged-in student"""
    # Ensure the user is a student
    if request.user.role != 'student':
        return render(request, 'materials/my_resources.html', {'error': 'Only students can view their resources'})
    
    student = request.user.student_profile
    
    # Get all modules the student is subscribed to
    subscribed_modules = StudentModule.objects.filter(
        student=student,
        is_hidden_by_student=False
    ).select_related('module').order_by('module__school__name', 'module__id')
    
    # Get all materials created by the student (both published and unpublished, but not deleted)
    all_materials = student.created_materials.filter(is_deleted=False).select_related('module')
    
    # Organizes materials by module
    modules_with_materials = []
    
    for subscription in subscribed_modules:
        module = subscription.module
        # Get materials for this module
        module_materials = all_materials.filter(module=module).order_by('-created_at')
        
        if module_materials.exists():
            modules_with_materials.append({
                'module': module,
                'materials': module_materials,
                'material_count': module_materials.count(),
            })
    
    # Also include materials not assigned to any module (private materials)
    private_materials = all_materials.filter(module__isnull=True).order_by('-created_at')
    
    context = {
        'modules_with_materials': modules_with_materials,
        'private_materials': private_materials,
        'total_materials': all_materials.count(),
    }
    
    return render(request, 'materials/my_resources.html', context)
@require_http_methods(["POST"])
def create_flashcard_set(request):
    """
    Create a new Flashcard Set.
    Expects a JSON payload with 'title', optional 'module_id', 'is_published', and a 'cards' array.
    """
    try:
        data = json.loads(request.body)
        title = data.get('title')
        module_id = data.get('module_id') # Optional module association
        is_published = data.get('is_published', False)
        cards_data = data.get('cards', [])

        if not title or not cards_data:
            return JsonResponse({"error": "Missing title or cards data"}, status=400)

        # Retrieve the Student instance associated with the currently logged-in User.
        # Updated to correctly use 'student_profile' as defined in accounts.models.py
        student = request.user.student_profile

        # Start a database transaction to ensure atomicity (all-or-nothing execution)
        with transaction.atomic():
            # 1. Create the base StudyMaterial record
            material = StudyMaterial.objects.create(
                title=title,
                material_type='flashcard',
                owner=student,
                module_id=module_id,
                is_published=is_published
            )

            # 2. Create the FlashcardSet metadata linked to the StudyMaterial
            flashcard_set = FlashcardSet.objects.create(study_material=material)

            # 3. Prepare and bulk create the individual Flashcards
            flashcards_to_create = []
            for index, card in enumerate(cards_data):
                flashcards_to_create.append(
                    Flashcard(
                        flashcard_set=flashcard_set,
                        front=card.get('front', ''),
                        back=card.get('back', ''),
                        order=card.get('order', index + 1) # Default to array index if order is not provided
                    )
                )
            # Use bulk_create for better database performance
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
    """
    Create a new Quiz.
    Expects a JSON payload with 'title', optional 'module_id', 'is_published', and a 'questions' array.
    """
    try:
        data = json.loads(request.body)
        title = data.get('title')
        module_id = data.get('module_id')
        is_published = data.get('is_published', False)
        questions_data = data.get('questions', [])

        if not title or not questions_data:
            return JsonResponse({"error": "Missing title or questions data"}, status=400)

        # Retrieve the Student instance
        student = request.user.student_profile

        # Start a database transaction
        with transaction.atomic():
            # 1. Create the base StudyMaterial record
            material = StudyMaterial.objects.create(
                title=title,
                material_type='quiz',
                owner=student,
                module_id=module_id,
                is_published=is_published
            )

            # 2. Create the Quiz metadata linked to the StudyMaterial
            quiz = Quiz.objects.create(study_material=material)

            # 3. Loop through to create questions and their respective answers
            for q_index, q_data in enumerate(questions_data):
                question = QuizQuestion.objects.create(
                    quiz=quiz,
                    question_text=q_data.get('question_text', ''),
                    question_type=q_data.get('question_type', 'single'),
                    order=q_data.get('order', q_index + 1)
                )

                # Prepare and bulk create answers for this specific question
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
    # Get subscribed modules
    subscribed_modules = StudentModule.objects.filter(student=student).select_related('module').order_by('module__school__name', 'module__id')
    context = {
        'subscribed': [sm.module for sm in subscribed_modules],
        'initial_module_id': module_id,
    }
    return render(request, 'materials/create_flashcard.html', context)

@login_required
def create_quiz_page(request, module_id=None):
    student = request.user.student_profile
    # Get subscribed modules
    subscribed_modules = StudentModule.objects.filter(student=student).select_related('module').order_by('module__school__name', 'module__id')
    context = {
        'subscribed': [sm.module for sm in subscribed_modules],
        'initial_module_id': module_id,
    }
    return render(request, 'materials/create_quiz.html', context)
@login_required
def view_flashcard(request, material_id):
    """Display a flashcard set"""
    material = StudyMaterial.objects.get(id=material_id, material_type='flashcard')
    
    # Check if the user has permission to view this material
    if material.owner != request.user.student_profile and not material.is_published:
        return render(request, 'materials/my_resources.html', {'error': 'You do not have permission to view this material'})
    
    flashcard_set = material.flashcard_set
    flashcards = flashcard_set.cards.all().order_by('order')
    
    context = {
        'flashcard_set': flashcard_set,
        'flashcards': flashcards,
    }
    
    return render(request, 'materials/view_flashcard.html', context)

@login_required
def view_quiz(request, material_id):
    """Display a quiz"""
    material = StudyMaterial.objects.get(id=material_id, material_type='quiz')
    
    # Check if the user has permission to view this material
    if material.owner != request.user.student_profile and not material.is_published:
        return render(request, 'materials/my_resources.html', {'error': 'You do not have permission to view this material'})
    
    quiz = material.quiz
    questions = quiz.questions.all().order_by('order')
    
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    
    return render(request, 'materials/view_quiz.html', context)