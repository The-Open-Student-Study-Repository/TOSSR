from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import School, Degree

# Create your tests here.


class TestLogIn(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')

        # Create school and degree for student
        self.school = School.objects.create(name='School of Computing Science')
        self.degree = Degree.objects.create(
            code='G400',
            name='Computing Science',
            degree_type='BSc (Hons)'
        )
        self.degree.schools.add(self.school)

        # Tier 1: Superuser
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123',
        )

        # Tier 2: Moderator
        self.moderator = User.objects.create_user(
            username='moderator',
            email='mod@test.com',
            password='mod123',
            role='moderator',
        )

        # Tier 3: Student
        self.student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='student123',
            role='student',
        )
        self.student = Student.objects.create(
            user=self.student_user,
            degree=self.degree,
            graduation_year=2026,
            bio='Test student',
        )

    def tearDown(self):
        User.objects.all().delete()
        School.objects.all().delete()
        Degree.objects.all().delete()

    def test_tier_1_login_redirects_to_admin(self):
        """Test Tier 1 (superuser) redirects to Django admin"""
        response = self.client.post(self.login_url, {
            'username': 'admin',
            'password': 'admin123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin:index'))

    def test_student_login_success(self):
        """Test Tier 2 (moderator) redirects to moderator dashboard"""
        response = self.client.post(self.login_url, {
            'username': 'moderator',
            'password': 'mod123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:moderator_dashboard'))

    def test_tier_3_login_redirects_to_student_dashboard(self):
        """Test Tier 3 (student) redirects to student dashboard"""
        response = self.client.post(self.login_url, {
            'username': 'student',
            'password': 'student123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:student_dashboard'))

    def test_get_tier_methods(self):
        """Test tier identification methods"""
        self.assertEqual(self.superuser.get_tier(), 1)
        self.assertEqual(self.superuser.get_tier_name(), 'Superuser')

        self.assertEqual(self.moderator.get_tier(), 2)
        self.assertEqual(self.moderator.get_tier_name(), 'Moderator')

        self.assertEqual(self.student_user.get_tier(), 3)
        self.assertEqual(self.student_user.get_tier_name(), 'Student')

    def test_student_required_decorator(self):
        """Test student_required decorator blocks non-students"""
        # Try to access student dashboard as moderator
        self.client.login(username='moderator', password='mod123')
        response = self.client.get(reverse('accounts:student_dashboard'))

        # Should redirect away
        self.assertEqual(response.status_code, 302)

    def test_moderator_required_decorator(self):
        """Test moderator_required decorator blocks non-moderators"""
        # Try to access moderator dashboard as student
        self.client.login(username='student', password='student123')
        response = self.client.get(reverse('accounts:moderator_dashboard'))

        # Should redirect away
        self.assertEqual(response.status_code, 302)

