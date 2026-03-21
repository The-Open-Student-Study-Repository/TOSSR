from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import StudyMaterial
from modules.models import StudentModule

def filter_materials(request):

    """
        FRONTEND DEVELOPER INSTRUCTIONS (AJAX Filtering API)
        —————————————————————————————————————————————————————————————————————————
        This is the API endpoint for the "Funnel" filtering tool on the materials page.
        As per the WAD2 rubric, please use Javascript/JQuery/AJAX to fetch data from this endpoint.

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
    
    # Organize materials by module
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
