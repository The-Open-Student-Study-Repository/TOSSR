from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
class User(AbstractUser):
    """
    Users are intended to be split into a 3 tier system:

    Tier 1L Django superusers
    """
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('moderator', 'Moderator'),
        # ('academic_staff', 'Academic Staff'), #TODO: Implement academic staff
    ]
    role = models.CharField(
        max_length=31,
        choices=ROLE_CHOICES,
        default='student',
        db_column='role',
        blank=True,  # Superusers/admins don't need a role
        null=True,
    )
    is_blocked = models.BooleanField(
        default=False,
        db_column='is_blocked',
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        db_column='username',
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

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_tier(self):
        """
        Return user's access tier:
        Tier 1: Django Superuser (database admin)
        Tier 2: TOSSR Moderator (content moderator)
        Tier 3: Regular users
        """
        if self.is_superuser:
            return 1
        elif self.role == 'moderator':
            return 2
        else:
            return 3

    def get_tier_name(self):
        tier_names = {
            1: 'Database Admin',      # ← Changed for clarity
            2: 'Content Moderator',   # ← Explicitly "Content Moderator"
            3: self.get_role_display(),
        }
        return tier_names.get(self.get_tier(), 'Unknown')

    def __str__(self):
        return f"Account:{self.username}, Role:{self.get_tier_name()}"

    class Meta:
        db_table='account'
        verbose_name = 'TOSSR Account'
        verbose_name_plural = 'TOSSR Accounts'

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
        db_column='graduation_year',
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
        return f"#{self.user_id} - {self.user.get_full_name()}"

    class Meta:
        db_table='student_profile'
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Student Profiles'