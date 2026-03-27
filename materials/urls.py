from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    # the 'filter/' is the actual URL path
    # name='filter_materials' meets the requirements of the {% url %} tag in the WAD2
    path('filter/', views.filter_materials, name='filter_materials'),
    path('api/flashcards/create/', views.create_flashcard_set, name='api_create_flashcard'),
    path('api/quiz/create/', views.create_quiz, name='api_create_quiz'),
    path('module/<str:module_id>/', views.browse_materials, name='browse_materials'),
    path('my-resources/', views.my_resources, name='my_resources'),
    path('create_flashcard/', views.create_flashcard_page, name='create_flashcard'),
    path('create_flashcard/<str:module_id>/', views.create_flashcard_page, name='create_flashcard_with_module'),
    path('create_quiz/', views.create_quiz_page, name='create_quiz'),
    path('create_quiz/<str:module_id>/', views.create_quiz_page, name='create_quiz_with_module'),
    path('flashcard/<int:material_id>/', views.view_flashcard, name='view_flashcard'),
    path('quiz/<int:material_id>/', views.view_quiz, name='view_quiz'),
]