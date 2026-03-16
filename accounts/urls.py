from django.urls import path
from . import views
from .views import logout

app_name = 'accounts'
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/step1/", views.signup_step1, name="signup_step1"),
    path("signup/step2/", views.signup_step2, name="signup_step2"),
    path("moderator/dashboard/", views.moderator_dashboard, name="moderator_dashboard"),
    path("moderator/materials/<int:material_id>/hide/", views.hide_material, name="hide_material"),
path("moderator/materials/<int:material_id>/unhide/", views.unhide_material, name="unhide_material"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path('logout/', logout, name='logout'),
]