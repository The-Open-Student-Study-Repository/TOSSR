def theme(request):
    return {
        "theme": request.COOKIES.get("theme", "light")
    }
def student_context(request):
    student = None
    if request.user.is_authenticated and hasattr(request.user, 'student_profile'):
        student = request.user.student_profile
    return {'student': student}