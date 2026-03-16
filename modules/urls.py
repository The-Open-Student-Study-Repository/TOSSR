from django.urls import path
from . import views
from .views import ModuleAutocompleteView

app_name = 'modules'

urlpatterns = [
    path("browse/", views.browse_modules, name="browse_modules"),
    path("autocomplete/module/", ModuleAutocompleteView.as_view(), name="module_autocomplete"),
]