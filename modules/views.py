from django.db import models
from django.shortcuts import render
from django_tomselect.autocompletes import AutocompleteModelView
from .models import Module, School

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

    return render(request, 'modules/browse.html', {
        'modules': modules,
        'levels': levels,
        'schools': schools,
        'credit_options': credit_options,
        'current_level': level,
        'current_school': school,
        'current_credits': credits,
        'current_q': q or '',
    })