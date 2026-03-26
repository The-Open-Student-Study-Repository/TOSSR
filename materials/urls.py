from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    # the 'filter/' is the actual URL path
    # name='filter_materials' meets the requirements of the {% url %} tag in the WAD2
    path('filter/', views.filter_materials, name='filter_materials'),
    path('api/flashcards/create/', views.create_flashcard_set, name='api_create_flashcard'),
    path('api/quiz/create/', views.create_quiz, name='api_create_quiz'),
    path('create_flashcard/',views.create_flashcard_page,name='create_flashcard'),
]