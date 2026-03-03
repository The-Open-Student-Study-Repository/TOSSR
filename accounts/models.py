from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
        ('academic_staff', 'Academic Staff'),
    ]
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default='student',
        db_column='role',
    )
    is_blocked = models.BooleanField(
        default=False,
        db_column='is_blocked',
    )

    first_name = models.CharField(
        max_length=255,
        blank=False,
        db_column='forename',
    )

    last_name = models.CharField(
        max_length=255,
        blank=False,
        db_column='surname',
    )
    def __str__(self):
        return f"Account:{self.username}, Role:{self.get_role_display()}"

    class Meta:
        db_table='account'
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='account_id',
        related_name='student_profile',
    )
    degree = models.ForeignKey(
        'modules.Degree',
        on_delete=models.PROTECT,
        db_column='degree_id',
    )
    graduation_year = models.IntegerField(
        db_column='graduation_date',
    )
    bio = models.CharField(
        max_length=255,
        default='This is my bio!',
        blank=True,
        db_column='bio',
    )
    can_publish = models.BooleanField(
        default=True,
        db_column='can_publish',
    )
    can_comment = models.BooleanField(
        default=True,
        db_column='can_comment',
    )
    def __str__(self):
        return f"{self.user.get_full_name()}. Graduating:{self.graduation_date}"

    class Meta:
        db_table='student_profile'
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Student Profiles'