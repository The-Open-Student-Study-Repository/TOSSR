from django.shortcuts import render

# Create your views here.
from django_tomselect.autocompletes import AutocompleteModelView
from .models import Module


class ModuleAutocompleteView(AutocompleteModelView):
    model = Module
    search_lookups = ["id__icontains", "name__icontains"]
    value_fields = ["id", "name", "level", "credits"]
    page_size = 20
    skip_authorization = True

    def hook_prepare_results(self, results):
        for item in results:
            item["display"] = f"{item['id']}: {item['name']}"
        return results