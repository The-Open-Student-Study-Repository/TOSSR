from django.contrib import admin
from .models import (
    StudyMaterial, PinnedMaterial, Quiz, QuizQuestion, QuizAnswer,
    FlashcardSet, Flashcard, Comment, Upvote, Report
)

admin.site.register(StudyMaterial)
admin.site.register(PinnedMaterial)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)
admin.site.register(FlashcardSet)
admin.site.register(Flashcard)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Report)