from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpStep1Form, SignUpStep2Form
from .models import User, Student


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

    return render(request, 'accounts/signup_step1.html'), {
        'form': form,
        'step': 1
    }

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

    return render(request, 'accounts/signup_step2.html', {
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