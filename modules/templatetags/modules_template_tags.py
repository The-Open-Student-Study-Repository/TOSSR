from django import template
from modules.models import PinnedModule,StudentModule

register = template.Library()

@register.inclusion_tag('modules/starred.html')
def get_starred_modules_list(user,current_module=None):

    user_subscriptions = set()
    user_favourites = set()
    if user.is_authenticated and user.role == 'student':
        student = user.student_profile
        user_subscriptions = set(
            StudentModule.objects.filter(student=student).values_list('module_id', flat=True)
        )
        user_favourites = set(
            PinnedModule.objects.filter(student=student)
        )
    for module in user_favourites:
        module.is_subscribed = module.module.id in user_subscriptions

    
    return {'starred': list(user_favourites)[:5],
            'current_module': current_module}