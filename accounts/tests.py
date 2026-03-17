from django.test import TestCase, Client, RequestFactory
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

class TestDegreeAutocomplete(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:degree_autocomplete')

        self.school = School.objects.create(name='School of Computing Science')

        self.degree1 = Degree.objects.create(
            code='G400', name='Computing Science', degree_type='BSc (Hons)'
        )
        self.degree2 = Degree.objects.create(
            code='G401', name='Software Engineering', degree_type='BSc (Hons)'
        )
        self.degree3 = Degree.objects.create(
            code='M100', name='Common Law', degree_type='LLB'
        )

    def tearDown(self):
        Degree.objects.all().delete()
        School.objects.all().delete()

    def test_search_returns_matching_degrees(self):
        response = self.client.get(self.url, {'q': 'Computing'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        codes = [r['code'] for r in data['results']]
        self.assertIn('G400', codes)
        self.assertNotIn('M100', codes)

    def test_search_returns_empty_for_no_match(self):
        response = self.client.get(self.url, {'q': 'Zoology'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['results']), 0)

    def test_search_is_case_insensitive(self):
        response = self.client.get(self.url, {'q': 'computing'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        codes = [r['code'] for r in data['results']]
        self.assertIn('G400', codes)

    def test_display_name_includes_degree_type(self):
        response = self.client.get(self.url, {'q': 'Computing'})
        data = response.json()
        result = next(r for r in data['results'] if r['code'] == 'G400')
        self.assertIn('BSc (Hons)', result['name'])

    def test_empty_query_returns_results(self):
        response = self.client.get(self.url, {'q': ''})
        self.assertEqual(response.status_code, 200)

    def test_no_duplicate_results(self):
        """Ensure distinct() prevents duplicate entries"""
        self.degree1.schools.add(self.school)
        response = self.client.get(self.url, {'q': 'Computing'})
        data = response.json()
        codes = [r['code'] for r in data['results']]
        self.assertEqual(len(codes), len(set(codes)))

class TestSignUpStep1(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:signup_step1')

    def test_step1_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_step1_valid_submission(self):
        response = self.client.post(self.url, {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'privacy_accepted': True,
        })
        self.assertRedirects(response, reverse('accounts:signup_step2'))
        self.assertIn('signup_step1', self.client.session)

    def test_step1_stores_session_data(self):
        self.client.post(self.url, {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'privacy_accepted': True,
        })
        session = self.client.session['signup_step1']
        self.assertEqual(session['username'], 'newuser')
        self.assertEqual(session['email'], 'new@test.com')

    def test_step1_duplicate_username(self):
        User.objects.create_user(username='taken', email='taken@test.com', password='pass1234')
        response = self.client.post(self.url, {
            'username': 'taken',
            'email': 'new@test.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'privacy_accepted': True,
        })
        self.assertEqual(response.status_code, 200)  # stays on page

    def test_step1_privacy_not_accepted(self):
        response = self.client.post(self.url, {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
        })
        self.assertEqual(response.status_code, 200)  # stays on page

    def test_step1_missing_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)  # stays on page


class TestSignUpStep2(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:signup_step2')

        self.school = School.objects.create(name='School of Computing Science')
        self.degree = Degree.objects.create(
            code='G400', name='Computing Science', degree_type='BSc (Hons)'
        )

    def tearDown(self):
        User.objects.all().delete()
        Student.objects.all().delete()
        Degree.objects.all().delete()
        School.objects.all().delete()

    def _set_step1_session(self):
        """Helper to simulate completing step 1"""
        session = self.client.session
        session['signup_step1'] = {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'testpass123',
        }
        session.save()

    def test_step2_redirects_without_step1(self):
        """Cannot access step 2 without completing step 1"""
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('accounts:signup_step1'))

    def test_step2_page_loads_with_session(self):
        self._set_step1_session()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_step2_creates_user_and_student(self):
        self._set_step1_session()
        response = self.client.post(self.url, {
            'forename': 'John',
            'surname': 'Smith',
            'degree': 'G400',
            'graduation_year': 2027,
            'bio': 'Test bio',
        })
        self.assertRedirects(response, reverse('accounts:login'))

        # Check user was created
        user = User.objects.get(username='newuser')
        self.assertEqual(user.email, 'new@test.com')
        self.assertEqual(user.role, 'student')

        # Check student profile was created
        student = Student.objects.get(user=user)
        self.assertEqual(student.degree.code, 'G400')
        self.assertEqual(student.graduation_year, 2027)
        self.assertEqual(student.bio, 'Test bio')

    def test_step2_clears_session_after_success(self):
        self._set_step1_session()
        self.client.post(self.url, {
            'forename': 'John',
            'surname': 'Smith',
            'degree': 'G400',
            'graduation_year': 2027,
            'bio': '',
        })
        self.assertNotIn('signup_step1', self.client.session)

    def test_step2_bio_optional(self):
        self._set_step1_session()
        response = self.client.post(self.url, {
            'forename': 'John',
            'surname': 'Smith',
            'degree': 'G400',
            'graduation_year': 2027,
            'bio': '',
        })
        self.assertRedirects(response, reverse('accounts:login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_step2_missing_required_fields(self):
        self._set_step1_session()
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)  # stays on page
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_step2_invalid_degree(self):
        self._set_step1_session()
        response = self.client.post(self.url, {
            'forename': 'John',
            'surname': 'Smith',
            'degree': 'XXXX',
            'graduation_year': 2027,
            'bio': '',
        })
        self.assertEqual(response.status_code, 200)  # stays on page
        self.assertFalse(User.objects.filter(username='newuser').exists())