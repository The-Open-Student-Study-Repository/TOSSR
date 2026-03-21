from django.urls import path
from . import views
from .views import ModuleAutocompleteView

app_name = 'modules'

urlpatterns = [
    path("browse/", views.browse_modules, name="browse_modules"),
    path("autocomplete/module/", ModuleAutocompleteView.as_view(), name="module_autocomplete"),
    path("subscribe/<str:module_id>/", views.toggle_subscribe_module, name="toggle_subscribe"),
    path("favourite/<str:module_id>/", views.toggle_favourite_module, name="toggle_favourite"),
    path("<str:module_id>/", views.module_detail, name="module_detail"),
]
