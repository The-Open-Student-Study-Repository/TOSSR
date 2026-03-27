from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django_tomselect.autocompletes import AutocompleteModelView
from .models import  School
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Exists, OuterRef, Prefetch
from modules.models import Module, StudentModule, PinnedModule
from materials.models import StudyMaterial, Upvote, Comment, SavedMaterial
class ModuleAutocompleteView(AutocompleteModelView):
    model = Module
    search_lookups = ["id__icontains", "name__icontains"]
    value_fields = ["id", "name", "level", "credits"]
    page_size = 21
    skip_authorization = True

    def get_queryset(self):
        qs = super().get_queryset().filter(is_archived=False)

        level = self.request.GET.get('level')
        school = self.request.GET.get('school')
        credits = self.request.GET.get('credits')

        if level:
            qs = qs.filter(level=level)
        if school:
            qs = qs.filter(school_id=school)
        if credits:
            qs = qs.filter(credits=credits)

        return qs.distinct()

    def hook_prepare_results(self, results):
        for item in results:
            item["display"] = f"{item['id']}: {item['name']}"
        return results


def browse_modules(request):
    modules = Module.objects.filter(is_archived=False).select_related('school')

    level = request.GET.get('level')
    selected_school = request.GET.get('school')
    credits = request.GET.get('credits')
    q = request.GET.get('q')

    if q:
        modules = modules.filter(
            models.Q(id__icontains=q) | models.Q(name__icontains=q)
        )
    if level:
        modules = modules.filter(level=level)
    if selected_school:
        modules = modules.filter(school_id=selected_school)
    if credits:
        modules = modules.filter(credits=credits)

    # Get distinct values for filter dropdowns
    levels = Module.objects.filter(is_archived=False).values_list('level', flat=True).distinct().order_by('level')
    schools = School.objects.filter(modules__is_archived=False).distinct().order_by('name')
    credit_options = Module.objects.filter(is_archived=False).values_list('credits', flat=True).distinct().order_by('credits')

    # Get user's subscriptions and favourites
    user_subscriptions = set()
    user_favourites = set()
    if request.user.is_authenticated and request.user.role == 'student':
        student = request.user.student_profile
        user_subscriptions = set(
            StudentModule.objects.filter(student=student).values_list('module_id', flat=True)
        )
        user_favourites = set(
            PinnedModule.objects.filter(student=student).values_list('module_id', flat=True)
        )

    # Add pagination
    paginator = Paginator(modules, 21)  # 21 modules per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Add subscription/favourite info to each module
    for module in page_obj:
        module.is_subscribed = module.id in user_subscriptions
        module.is_favourited = module.id in user_favourites

    return render(request, 'modules/findmodules.html', {
        'page_obj': page_obj,
        'levels': levels,
        'schools': schools,
        'credit_options': credit_options,
        'level': level,
        'selected_school': selected_school,
        'credits': credits,
        'q': q or '',
    })


@login_required
def toggle_subscribe_module(request, module_id):
    """Toggle subscription to a module"""
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can subscribe to modules'}, status=403)

    module = get_object_or_404(Module, id=module_id)
    student = request.user.student_profile

    subscription, created = StudentModule.objects.get_or_create(
        student=student,
        module=module
    )

    if not created:
        # Check if user has published materials to this module
        has_materials = StudyMaterial.objects.filter(
            module=module, owner=student, is_published=True
        ).exists()
        if has_materials:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Cannot unsubscribe from a module you have published materials to'},
                                    status=400)
            messages.error(request, 'Cannot unsubscribe from a module you have created materials for.')
            return redirect(request.META.get('HTTP_REFERER', 'modules:browse_modules'))

        # Already subscribed, so unsubscribe
        subscription.delete()
        PinnedModule.objects.filter(student=student, module=module).delete()
        is_subscribed = False
    else:
        is_subscribed = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'is_subscribed': is_subscribed})

    # Preserve the current page and filters
    query_params = request.GET.urlencode()
    if query_params:
        return redirect(f"{request.META.get('HTTP_REFERER', 'modules:browse_modules')}?{query_params}")
    return redirect(request.META.get('HTTP_REFERER', 'modules:browse_modules'))


@login_required
def toggle_favourite_module(request, module_id):
    """Toggle favourite/pinned status of a module"""
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can favourite modules'}, status=403)

    module = get_object_or_404(Module, id=module_id)
    student = request.user.student_profile

    favourite, created = PinnedModule.objects.get_or_create(
        student=student,
        module=module
    )

    if not created:
        # Already favourited, so unfavourite
        favourite.delete()
        is_favourited = False
    else:
        is_favourited = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'is_favourited': is_favourited})

    # Preserve the current page and filters
    query_params = request.GET.urlencode()
    if query_params:
        return redirect(f"{request.META.get('HTTP_REFERER', 'modules:browse_modules')}?{query_params}")
    return redirect(request.META.get('HTTP_REFERER', 'modules:browse_modules'))

@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id, is_archived=False)

    is_subscribed = False
    is_favourited = False
    saved_material_ids = []

    materials = module.materials.filter(
        is_published=True, is_deleted=False, is_hidden_by_admin=False
    ).select_related('owner__user').annotate(
        upvote_count=Count('upvotes'),
        comment_count=Count('comments'),
    )

    if request.user.is_authenticated and request.user.role == 'student':
        student = request.user.student_profile
        is_subscribed = StudentModule.objects.filter(student=student, module=module).exists()
        is_favourited = PinnedModule.objects.filter(student=student, module=module).exists()

        # Add annotation for upvote state
        materials = materials.annotate(
            user_has_upvoted=Exists(
                Upvote.objects.filter(student=student, study_material=OuterRef('pk'))
            )
        )

        # Get IDs of materials the student has saved in this module
        saved_material_ids = list(
            SavedMaterial.objects.filter(student=student, study_material__module=module)
            .values_list('study_material_id', flat=True)
        )

    # Prefetch comments for each material
    materials = materials.prefetch_related(
        Prefetch(
            'comments',
            queryset=Comment.objects.select_related('student__user').order_by('-created_at'),
            to_attr='visible_comments'
        )
    )

    context = {
        'module': module,
        'materials': materials,
        'is_subscribed': is_subscribed,
        'is_favourited': is_favourited,
        'saved_material_ids': saved_material_ids,
    }

    return render(request, 'modules/module_detail.html', context)
@login_required
def toggle_archive_module(request, module_id):
    if request.user.role != 'student':
        return JsonResponse({'error': 'Only students can archive modules'}, status=403)

    student = request.user.student_profile
    subscription = get_object_or_404(StudentModule, student=student, module_id=module_id)

    subscription.is_hidden_by_student = not subscription.is_hidden_by_student
    subscription.save()

    return redirect(request.META.get('HTTP_REFERER', 'materials:my_resources'))