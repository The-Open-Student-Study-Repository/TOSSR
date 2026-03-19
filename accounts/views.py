from typing import Any
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from materials.models import StudyMaterial
from .forms import SignUpStep1Form, SignUpStep2Form
from .models import User, Student
from  modules.models import Degree
from .decorators import student_required, moderator_required
from django_tomselect.autocompletes import AutocompleteModelView

# Create your views here.


def signup_step1(request):
    """
    Step 1: Username, email and password.
    Validates the uniqueness of the username and email.
    """
    if request.method == "POST":
        form = SignUpStep1Form(request.POST)

        if form.is_valid():
            request.session['signup_step1'] = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']
            }

            return redirect('accounts:signup_step2')

    else:
        form = SignUpStep1Form()

    return render(request, 'accounts/signup/signup_step1.html', {
        'form': form,
        'step': 1
    })

def signup_step2(request):
    """
    Step 2: Name, degree, bio
    Separated in order to have a cleaner UI and easier account validation.
    """

    if 'signup_step1' not in request.session:
        return redirect('accounts:signup_step1')

    if request.method == "POST":
        form = SignUpStep2Form(request.POST)

        if form.is_valid():

            step1_data = request.session['signup_step1']

            user = User.objects.create_user(
                username=step1_data['username'],
                email=step1_data['email'],
                password=step1_data['password'],
                first_name=form.cleaned_data['forename'],
                last_name=form.cleaned_data['surname'],
                role='student'
            )

            Student.objects.create(
                user=user,
                degree=form.cleaned_data['degree'],
                graduation_year=form.cleaned_data['graduation_year'],
                bio=form.cleaned_data['bio'],
            )

            del request.session['signup_step1']

            return redirect('accounts:login')

    else:
        form = SignUpStep2Form()

    return render(request, 'accounts/signup/signup_step2.html', {
        'form': form,
        'step': 2
    })


def login_view(request):
    """
    Login: redirect after success undecided for now
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin:index')
        elif request.user.role == 'moderator':
            return redirect('accounts:moderator_dashboard')
        else:  # student
            return redirect('accounts:student_dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and isinstance(user, User):
            if user.is_blocked:
                return render(request, 'accounts/login.html', {
                    'error': 'Your account has been blocked'
                })

            login(request, user)
            if user.is_superuser:
                return redirect('admin:index')
            elif user.role == 'moderator':
                return redirect('accounts:moderator_dashboard')
            else:
                return redirect('accounts:student_dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'accounts/login.html')

def logout(request):
    """
    Logs the user out and clears the session
    
    """
    request.session.flush()

    return redirect('/accounts/login/')




@student_required
def student_dashboard(request):
    """Tier 3: Student dashboard"""
    student = request.user.student_profile

    return render(request, 'accounts/placeholder.html', {
        'user': request.user,
        'student': student,
        'message': f'Student Dashboard for {student.degree}'
    })


@moderator_required
def moderator_dashboard(request):
    """Tier 2: Moderator dashboard for content moderation"""

    # Get materials that need attention
    flagged_materials = StudyMaterial.objects.filter(
        is_hidden_by_admin=False
    ).select_related('owner', 'module')[:20]

    hidden_materials = StudyMaterial.objects.filter(
        is_hidden_by_admin=True
    ).select_related('owner', 'module')[:20]

    recent_materials = StudyMaterial.objects.filter(
        is_published=True,
        is_deleted=False
    ).order_by('-created_at')[:10]

    stats = {
        'total_materials': StudyMaterial.objects.filter(is_deleted=False).count(),
        'published_materials': StudyMaterial.objects.filter(
            is_published=True,
            is_deleted=False
        ).count(),
        'hidden_materials': StudyMaterial.objects.filter(is_hidden_by_admin=True).count(),
        'total_students': User.objects.filter(role='student').count(),
    }
    #TODO: MAKE SURE WE MAKE A MOD DASHBOARD
    return render(request, 'accounts/moderator_dashboard.html', {
        'flagged_materials': flagged_materials,
        'hidden_materials': hidden_materials,
        'recent_materials': recent_materials,
        'stats': stats,
    })


@moderator_required
def hide_material(request, material_id):
    """Hide a study material (Tier 2 only)"""
    material = get_object_or_404(StudyMaterial, id=material_id)
    material.is_hidden_by_admin = True
    material.save()
    return redirect('accounts:moderator_dashboard')

@moderator_required
def unhide_material(request, material_id):
    """Unhide a study material (Tier 2 only)"""
    material = get_object_or_404(StudyMaterial, id=material_id)
    material.is_hidden_by_admin = False
    material.save()
    return redirect('accounts:moderator_dashboard')


@login_required
def download_my_data(request):
    """GDPR: Export all user data (Tier 2 & 3)"""
    user: User = request.user

    # Superusers don't use this feature
    if user.is_superuser:
        return redirect('admin:index')

    data: dict[str, Any] = {
        'profile': {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'tier': user.get_tier_name(),
            'role': user.role,
            'date_joined': user.created_at.isoformat(),
        }
    }

    if user.role == 'student':
        student = user.student_profile

        data['profile'].update({
            'degree': student.degree.get_full_name(),
            'graduation_year': student.graduation_year,
            'bio': student.bio,
        })

        data['modules'] = [
            {
                'code': sm.module.id,
                'name': sm.module.name,
            }
            for sm in student.studentmodule_set.all()
        ]

        data['materials_created'] = [
            {
                'title': mat.title,
                'type': mat.material_type,
                'created': mat.created_at.isoformat(),
            }
            for mat in student.created_materials.all()
        ]

    response = JsonResponse(data)
    response['Content-Disposition'] = f'attachment; filename="tossr_data_{user.username}.json"'
    return response



@login_required
def anonymise_account(request):
    """GDPR: Right to be forgotten (Tier 2 & 3)"""

    # Superusers don't use this feature
    if request.user.is_superuser:
        return redirect('admin:index')

    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)

        if user:
            if user.role == 'student':
                student = user.student_profile

                student.created_materials.filter(
                    Q(is_published=False) | Q(module__isnull=True) | Q(is_deleted=True)
                ).delete()

                student.bio = ""
                student.save()

            user.username = f"deleted_user_{user.id}"
            user.email = f"deleted_{user.id}@deleted.com"
            user.first_name = "Deleted"
            user.last_name = "User"
            user.is_active = False
            user.save()

            logout(request)
            return redirect('account_deleted')
        else:
            return render(request, 'accounts/delete_account.html', {
                'error': 'Incorrect password'
            })

    return render(request, 'accounts/delete_account.html')

<<<<<<< HEAD
class DegreeAutocompleteView(AutocompleteModelView):
    model = Degree
    search_lookups = ["name__icontains"]
    value_fields = ["code", "name", "degree_type"]
    page_size = 20
    skip_authorization = True

    def hook_prepare_results(self, results):
        for item in results:
            item["name"] = f"{item.get('name', '')} {item.get('degree_type', '')}".strip()
        return results
=======
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('accounts:login'))
>>>>>>> 6b3170f (settings frontend started)
