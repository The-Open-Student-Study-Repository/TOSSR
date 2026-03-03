from django.db import models


class StudyMaterial(models.Model):
    """
    Core entity of TOSSR. Students create materials and publish them to modules.
    Materials can be published (visible to everyone in the module) or private.
    """

    title = models.CharField(
        max_length=255,
        db_column='title',
        help_text='Name of the flashcard set or quiz',
    )

    MATERIAL_TYPE_CHOICES = [
        ('flashcard', 'Flashcard'),
        ('quiz', 'Quiz'),
    ]

    material_type = models.CharField(
        max_length=20,
        choices=MATERIAL_TYPE_CHOICES,  # Enforces your check constraint
        db_column='material_type',
        help_text='Type of study material',
    )

    owner = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,  # Matches your 'on delete cascade'
        db_column='owner_id',
        related_name='created_materials',
        help_text='Student who created this material',
    )

    module = models.ForeignKey(
        'modules.Module',
        on_delete=models.SET_NULL,  # Matches your 'on delete set null'
        null=True,  # Matches your SQL 'null'
        blank=True,
        db_column='module_id',
        related_name='materials',
        help_text='Module this material belongs to. NULL means private/unassigned.',
    )

    is_published = models.BooleanField(
        default=False,
        db_column='is_published',
        help_text='If True, material is visible to all users in the module',
    )

    is_deleted = models.BooleanField(
        default=False,
        db_column='is_deleted',
        help_text='Soft delete - material marked as deleted but not removed from DB',
    )

    is_hidden_by_admin = models.BooleanField(
        default=False,
        db_column='is_hidden_by_admin',
        help_text='Admin has hidden this material due to inappropriate content',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Automatically set when created
        db_column='created_at',
    )

    pinned_by = models.ManyToManyField(
        'accounts.Student',
        through='PinnedMaterial',
        related_name='pinned_material',
        help_text='Students who starred this material for quick access',
    )

    def __str__(self):
        return f"{self.title} ({self.get_material_type_display()})"

    class Meta:
        db_table = 'study_material'
        verbose_name = 'Study Material'
        verbose_name_plural = 'Study Materials'
        indexes = [
            models.Index(fields=['owner'], name='idx_material_owner'),
            models.Index(fields=['module', 'is_published', 'is_deleted', 'is_hidden_by_admin'],
                         name='idx_material_module_pub'),
        ]


class PinnedMaterial(models.Model):
    """
    Junction table for materials students have starred/pinned to favorites.
    """
    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        db_column='student_id',
    )

    study_material = models.ForeignKey(
        StudyMaterial,
        on_delete=models.CASCADE,
        db_column='material_id',
    )

    def __str__(self):
        return f"{self.student.user.username} pinned {self.study_material.title}"

    class Meta:
        db_table = 'pinned_material'
        unique_together = [['student', 'study_material']]
        verbose_name = 'Pinned Material'
        verbose_name_plural = 'Pinned Materials'

class Comment(models.Model):
    """
    Comments on study materials.
    """

    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        db_column='student_id',
        related_name='comments',
    )

    study_material = models.ForeignKey(
        StudyMaterial,
        on_delete=models.CASCADE,
        db_column='material_id',
        related_name='comments',
    )

    content = models.CharField(
        max_length=3000,
        db_column='content',
        help_text='Content of comment (Max 3000 characters)',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
    )

    def __str__(self):
        return f"Comment by {self.student.user.username} on {self.study_material.title}"

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        indexes = [
            models.Index(fields=['study_material'], name='idx_comment_material'),
        ]
        ordering = ['-created_at']


class Upvote(models.Model):
    """
    Upvotes on study materials.

    Students can upvote helpful materials. Each student can only upvote once.
    """
    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,  # Matches your 'on delete cascade'
        db_column='student_id',
    )

    study_material = models.ForeignKey(
        StudyMaterial,
        on_delete=models.CASCADE,  # Matches your 'on delete cascade'
        db_column='material_id',
        related_name='upvotes',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
    )

    def __str__(self):
        return f"{self.student.user.username} upvoted {self.study_material.title}"

    class Meta:
        db_table = 'upvote'
        unique_together = [['student', 'study_material']]
        verbose_name = 'Upvote'
        verbose_name_plural = 'Upvotes'
        indexes = [
            models.Index(fields=['study_material'], name='idx_upvote_material'),
        ]


class Report(models.Model):
    """
    Reports of inappropriate content
    """
    REPORT_REASON_CHOICES = [
        ('inappropriate', 'Inappropriate Content'),
        ('spam', 'Spam'),
        ('incorrect', 'Incorrect Information'),
        ('offensive', 'Offensive/Harassment'),
        ('other', 'Other'),
    ]

    # Student who reported
    reporter = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        db_column='reporter_id',
        related_name='reports_made',
    )

    # Material being reported
    study_material = models.ForeignKey(
        StudyMaterial,
        on_delete=models.CASCADE,
        db_column='material_id',
        related_name='reports',
    )

    # Reason for report
    reason = models.CharField(
        max_length=20,
        choices=REPORT_REASON_CHOICES,
        db_column='reason',
    )

    # Optional details
    details = models.TextField(
        max_length=500,
        blank=True,
        db_column='details',
        help_text='Additional details about the report',
    )

    # When reported
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
    )

    is_reviewed = models.BooleanField(
        default=False,
        db_column='is_reviewed',
        help_text='Has an admin reviewed this report?',
    )

    def __str__(self):
        return f"Report by {self.reporter.user.username} on {self.study_material.title}"

    class Meta:
        db_table = 'report'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        # Prevent duplicate reports.
        unique_together = [['reporter', 'study_material']]


class Quiz(models.Model):
    """
    Quiz metadata
    """
    study_material = models.OneToOneField(
        StudyMaterial,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='material_id',
        related_name='quiz',
    )

    def __str__(self):
        return f"Quiz: {self.study_material.title}"

    class Meta:
        db_table = 'quiz'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class QuizQuestion(models.Model):
    """
    Individual question in a quiz.
    Each question can be single-answer or multiple-answer.
    """
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        db_column='quiz_id',
        related_name='questions',
    )

    question_text = models.TextField(
        max_length=1000,
        db_column='question_text',
        help_text='Question text - Markdown supported',
    )

    QUESTION_TYPE_CHOICES = [
        ('single', 'Single Answer - Pick One'),
        ('multiple', 'Multiple Answers - Select All That Apply'),
    ]

    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPE_CHOICES,
        default='single',
        db_column='question_type',
        help_text='Single answer (radio buttons) or multiple answers (checkboxes)',
    )

    order = models.IntegerField(
        db_column='order',
        help_text='Display order of questions',
    )

    def __str__(self):
        return f"Q{self.order}: {self.question_text[:50]}"

    class Meta:
        db_table = 'quiz_question'
        ordering = ['order']
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'


class QuizAnswer(models.Model):
    """
    Possible answer to a quiz question.
    """
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        db_column='question_id',
        related_name='answers',
    )

    answer_text = models.CharField(
        max_length=500,
        db_column='answer_text',
        help_text='Answer text - Markdown supported',
    )

    is_correct = models.BooleanField(
        default=False,
        db_column='is_correct',
        help_text='True if this is a correct answer',
    )

    order = models.IntegerField(
        db_column='order',
        help_text='Display order of answers',
    )

    def __str__(self):
        correct = "✓" if self.is_correct else "✗"
        return f"{correct} {self.answer_text[:30]}"

    class Meta:
        db_table = 'quiz_answer'
        ordering = ['order']
        verbose_name = 'Quiz Answer'
        verbose_name_plural = 'Quiz Answers'


class FlashcardSet(models.Model):
    """
    Flashcard set metadata
    """
    study_material = models.OneToOneField(
        StudyMaterial,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='material_id',
        related_name='flashcard_set',
    )

    def __str__(self):
        return f"Flashcard Set: {self.study_material.title}"

    class Meta:
        db_table = 'flashcard_set'
        verbose_name = 'Flashcard Set'
        verbose_name_plural = 'Flashcard Sets'


class Flashcard(models.Model):
    """
    Individual flashcard in a set.
    """
    flashcard_set = models.ForeignKey(
        FlashcardSet,
        on_delete=models.CASCADE,
        db_column='set_id',
        related_name='cards',
    )

    front = models.TextField(
        max_length=500,
        db_column='front',
        help_text='Front of card (question/term) - Markdown supported',
    )

    back = models.TextField(
        max_length=1000,
        db_column='back',
        help_text='Back of card (answer/definition) - Markdown supported',
    )

    order = models.IntegerField(
        db_column='order',
        help_text='Display order in the set',
    )

    def __str__(self):
        return f"Card {self.order}: {self.front[:30]}"

    class Meta:
        db_table = 'flashcard'
        ordering = ['order']
        verbose_name = 'Flashcard'
        verbose_name_plural = 'Flashcards'