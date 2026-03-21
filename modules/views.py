from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django_tomselect.autocompletes import AutocompleteModelView
from .models import Module, School, StudentModule, PinnedModule

class ModuleAutocompleteView(AutocompleteModelView):
    model = Module
    search_lookups = ["id__icontains", "name__icontains"]
    value_fields = ["id", "name", "level", "credits"]
    page_size = 20
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

    # Get filter values from query params
    level = request.GET.get('level')
    school = request.GET.get('school')
    credits = request.GET.get('credits')
    q = request.GET.get('q')

    if q:
        modules = modules.filter(
            models.Q(id__icontains=q) | models.Q(name__icontains=q)
        )
    if level:
        modules = modules.filter(level=level)
    if school:
        modules = modules.filter(school_id=school)
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
    paginator = Paginator(modules, 20)  # 20 modules per page
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
        'school': school,
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
        # Already subscribed, so unsubscribe
        subscription.delete()
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
