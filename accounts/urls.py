from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/step1/", views.signup_step1, name="signup_step1"),
    path("signup/step2/", views.signup_step2, name="signup_step2"),
    path("placeholder/", views.placeholder_view, name="placeholder"),

]