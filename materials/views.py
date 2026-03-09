from django.shortcuts import render
from django.http import JsonResponse
from .models import StudyMaterial

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
