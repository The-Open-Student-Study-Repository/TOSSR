from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/step1/", views.signup_step1, name="signup_step1"),
    path("signup/step2/", views.signup_step2, name="signup_step2"),
    path("moderator/dashboard/", views.moderator_dashboard, name="moderator_dashboard"),
    path("moderator/materials/<int:material_id>/hide/", views.hide_material, name="hide_material"),
    path("moderator/materials/<int:material_id>/unhide/", views.unhide_material, name="unhide_material"),
    path("moderator/report/<int:report_id>/review/", views.review_report, name='review_report'),
    path("moderator/comment/<int:comment_id>/hide/", views.hide_comment, name='hide_comment'),
    path("moderator/comment/<int:comment_id>/restore/", views.restore_comment, name='restore_comment'),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("autocomplete/degree/", views.DegreeAutocompleteView.as_view(), name="degree_autocomplete"),
    path("settings/", views.settings, name="settings"),
    path("logout/", views.user_logout, name="logout"),
    path("set-theme/<str:theme>/", views.set_theme, name="set_theme"),
    path("download-my-data/", views.download_my_data, name="download_my_data"),
    path("anonymise-account/", views.anonymise_account, name="anonymise_account"),
    path("account-deleted/", TemplateView.as_view(template_name="accounts/account_deleted.html"), name="account_deleted"),
]