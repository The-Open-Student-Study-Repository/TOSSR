from django.urls import path
from .views import ModuleAutocompleteView

app_name = 'modules'
urlpatterns = [
    path("autocomplete/module/", ModuleAutocompleteView.as_view(), name="module_autocomplete"),
]