from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('filter/', views.filter_materials, name='filter_materials'),
    path('api/flashcards/create/', views.create_flashcard_set, name='api_create_flashcard'),
    path('api/quiz/create/', views.create_quiz, name='api_create_quiz'),
    path('module/<str:module_id>/', views.browse_materials, name='browse_materials'),
    path('my-resources/', views.my_resources, name='my_resources'),
    path('create/flashcard/', views.create_flashcard_page, name='create_flashcard'),
    path('create/flashcard/<str:module_id>/', views.create_flashcard_page, name='create_flashcard_with_module'),
    path('create/quiz/', views.create_quiz_page, name='create_quiz'),
    path('create/quiz/<str:module_id>/', views.create_quiz_page, name='create_quiz_with_module'),
    path('flashcard/<int:material_id>/', views.view_flashcard, name='view_flashcard'),
    path('quiz/<int:material_id>/', views.view_quiz, name='view_quiz'),
    path('upvote/<int:material_id>/', views.toggle_upvote, name='toggle_upvote'),
    path('comment/<int:material_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('toggle-publish/<int:material_id>/', views.toggle_publish_material, name='toggle_publish'),
    path('delete/<int:material_id>/', views.delete_material, name='delete_material'),
    path('report/material/<int:material_id>/', views.report_material, name='report_material'),
    path('report/comment/<int:comment_id>/', views.report_comment, name='report_comment'),
    path('save/<int:material_id>/', views.toggle_save_material, name='toggle_save_material'),
]