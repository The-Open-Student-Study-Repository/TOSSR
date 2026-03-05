from typing import Any

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpStep1Form, SignUpStep2Form
from .models import User, Student
import json

# Create your views here.

def login_view(request):
    return render(request, "accounts/login.html")

def signup_view(request):
    return render(request, "accounts/signup_step1.html")

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

            return redirect('signup_step2')

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
    :param request:
    :return:
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
                first_name=step1_data['forename'],
                last_name=step1_data['surname'],
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
            if user.is_staff:
                return redirect('/admin/') #TODO: decide on landing page
            else:
                return redirect('accounts:placeholder')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login/')
def placeholder_view(request):
    if request.user.is_staff:
        return redirect('/admin/')
    """
    Temporary placeholder dashboard for testing
    """
    return render(request, 'accounts/placeholder.html', {
        'user': request.user,
        'student': request.user.student_profile,
    })


@login_required
def download_my_data(request):
    """Required for GDPR Compliancy"""
    user: User = request.user
    data: dict[str, Any] = {
        'profile': {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
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
        data['comments'] = [
            {
                'content': c.content,
                'date': c.created_at.isoformat(),
            }
            for c in student.comments.all()
        ]




    response = JsonResponse(data)
    response['Content-Disposition'] = f'attachment; filename="tossr_data_{user.username}.json"'
    return response



@login_required
def anonymise_account(request):
    """
    GDPR Compliancy
    """
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user:
            user.username = f"deleted_user_{user.id}"
            user.email = f"deleted_{user.id}@deleted.com"
            user.first_name = "Deleted"
            user.last_name = "User"
            user.is_active = False
            user.save()
            if user.role == 'student':
                student = user.student_profile
                student.student_profile.bio = ""

                student.created_materials.filter(is_published=False).delete()
                student.created_materials.filter(module__isnull=True).delete()
                student.created_materials.filter(is_deleted=True).delete()
                student.save()
            logout(request)
            return redirect('account_deleted')
        else:
            # TODO: make profile delete page
            return render(request, 'accounts/delete_account.html', {
                'error': 'Incorrect password'
            })

    return render(request, 'accounts/delete_account.html')