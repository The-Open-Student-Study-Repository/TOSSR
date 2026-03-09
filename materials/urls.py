from django.urls import path
from . import views

urlpatterns = [
    # the 'filter/' is the actual URL path
    # name='filter_materials' meets the requirements of the {% url %} tag in the WAD2
    path('filter/', views.filter_materials, name='filter_materials'),
]