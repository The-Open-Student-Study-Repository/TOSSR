from django import template
from modules.models import PinnedModule

register = template.Library()

@register.inclusion_tag('modules/starred.html')
def get_starred_modules_list(current_module=None):
    return {'starred': PinnedModule.objects.all()[:5],
            'current_module': current_module}