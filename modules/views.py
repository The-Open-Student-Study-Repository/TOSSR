from django.shortcuts import render
from django.core.paginator import Paginator
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
    
    # Pagination
    paginator = Paginator(modules, 12)  # 12 modules per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'schools': School.objects.all(),
        'school': school,
        'level': level,
    }
    return render(request, 'modules/findmodules.html', context)