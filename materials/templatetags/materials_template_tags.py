from django import template
from materials.models import PinnedMaterial

register = template.Library()

@register.inclusion_tag('materials/starred.html')
def get_starred_materials_list(current_material=None):
    return {'starred': PinnedMaterial.objects.all()[:5],
            'current_material': current_material}