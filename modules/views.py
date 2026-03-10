from django.shortcuts import render
from .models import Module, School

def module_list(request):
    modules = Module.objects.filter(is_archived=False).select_related('school')
    
    # Filter by school if provided
    school = request.GET.get('school')
    if school:
        modules = modules.filter(school_id=school)
    
    # Filter by level if provided
    level = request.GET.get('level')
    if level:
        modules = modules.filter(level=level)
    
    context = {
        'modules': modules,
        'schools': School.objects.all(),
    }
    return render(request, 'modules/mymodules.html', context)