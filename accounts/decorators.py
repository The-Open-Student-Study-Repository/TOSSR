from django.shortcuts import redirect
from functools import wraps


def student_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        if request.user.is_superuser:
            return redirect('admin:index')

        if request.user.role != 'student':
            return redirect('accounts:moderator_dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def moderator_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        if request.user.is_superuser:
            return redirect('admin:index')

        if request.user.role != 'moderator':
            return redirect('accounts:student_dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def tier_2_or_higher(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        if not (request.user.is_superuser or request.user.role == 'moderator'):
            return redirect('accounts:student_dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper