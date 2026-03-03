from django.db import models

class School(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True,
        db_column='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        db_table = 'school'

class Degree(models.Model):

    code = models.CharField(
        max_length=4,
        primary_key=True,
        db_column='id',
        help_text='Degree code. Check UofG: https://www.gla.ac.uk/undergraduate/'
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        db_column='name',
        help_text='Full degree name.'
    )

    DEGREE_TYPE_CHOICES = [
        ('BSc', 'Bachelor of Science'),
        ('MSci', 'Master in Science'),
        ('MA', 'Master of Arts'),
        ('MA(SocSci)', 'Master of Arts (Social Sciences)'),
        ('BEng', 'Bachelor of Engineering'),
        ('MEng', 'Master of Engineering'),
        ('LLB', 'Bachelor of Laws'),
        ('BAcc', 'Bachelor of Accountancy'),
        ('BFin', 'Bachelor of Finance'),
        ('MBChB', 'Bachelor of Medicine, Bachelor of Surgery'),
        ('BDS', 'Bachelor of Dental Surgery'),
        ('BVMS', 'Bachelor of Veterinary Medicine & Surgery'),
        ('BN', 'Bachelor of Nursing'),
        ('BMus', 'Bachelor of Music'),
        ('MEduc', 'Master of Education'),
        ('MDTechEd', 'Master of Design & Technology Education'),
        ('BD', 'Bachelor of Divinity'),
        ('BA', 'Bachelor of Arts'),
        ('CertHE', 'Certificate of Higher Education'),
        ('LSc', 'Laurea in Statistica'),  # For Bologna double degree
    ]

    degree_type = models.CharField(
        max_length=15,  # Increased for 'MA(SocSci)'
        choices=DEGREE_TYPE_CHOICES,
        db_column='degree_type',
        null=True,
        blank=True,
        help_text='Degree type (can be null due to some dual international degrees)'
    )

    schools = models.ManyToManyField(
        School,
        db_table='degree_school',
        related_name='degrees',
    )

    def get_full_name(self):
        """Returns full degree name e.g. BSc Computing Science'"""
        return f"{self.degree_type} {self.name}"

    def __str__(self):
        return self.get_full_name()

    class Meta:
        db_table = 'degree'
        verbose_name = 'Degree Program'
        verbose_name_plural = 'Degree Programs'

class Module(models.Model):

    id = models.CharField(
        max_length=16,
        primary_key=True,
        db_column='id',
        help_text='Module code. Check UofG course content page: https://www.gla.ac.uk/coursecatalogue/.'
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        db_column='name',
        help_text='Module name'
    )

    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        db_column='school_id',
        related_name='modules',
    )

    level = models.PositiveIntegerField(
        db_column='level',
        help_text='Module level 1-5'
    )

    credits = models.PositiveIntegerField(
        db_column='credits',
        help_text='Module credits'
    )

    is_archived = models.BooleanField(
        default=False,
        db_column='is_archived',
        help_text='If true, model is archived and not shown unless filtered for. Does not accept new study materials.be'
    )

    subscribers = models.ManyToManyField(
        'accounts.Student',
        through='StudentModule',
        related_name='subscribed_modules',
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        db_table = 'module'
        unique_together = [['name', 'school']]
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'


class StudentModule(models.Model):
    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        db_column='student_id',
    )

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        db_column='module_id',
    )

    is_hidden_by_student = models.BooleanField(
        default=False,
        db_column='is_archived',
        help_text='Student can archive modules to hide them without unsubscribing',
    )

    def __str__(self):
        return f"{self.student.id}: {self.module.id}"

    class Meta:
        db_table = 'student_module'
        unique_together = [['student', 'module']]
        verbose_name = 'Student Module Subscription'
        verbose_name_plural = 'Student Module Subscriptions'


class PinnedModule(models.Model):
    """
    Junction table for modules students have favorited/pinned.
    """
    student = models.ForeignKey(
        'accounts.Student',
        on_delete=models.CASCADE,
        db_column='student_id',
    )

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        db_column='module_id',
    )

    def __str__(self):
        return f"{self.student.user.username} pinned {self.module.id}"

    class Meta:
        db_table = 'pinned_module'
        unique_together = [['student', 'module']]
        verbose_name = 'Pinned Module'
        verbose_name_plural = 'Pinned Modules'