from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from .models import School, Module, StudentModule, PinnedModule

class TestModuleAutocomplete(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('modules:module_autocomplete')

        self.school = School.objects.create(name='School of Computing Science')
        self.school2 = School.objects.create(name='School of Mathematics')

        self.module1 = Module.objects.create(
            id='COMPSCI4009', name='Algorithmics', school=self.school, level=4, credits=20
        )
        self.module2 = Module.objects.create(
            id='COMPSCI2024', name='Web App Development', school=self.school, level=2, credits=20
        )
        self.module3 = Module.objects.create(
            id='MATH1017', name='Calculus', school=self.school2, level=1, credits=20
        )

    def tearDown(self):
        Module.objects.all().delete()
        School.objects.all().delete()

    def test_search_by_name(self):
        response = self.client.get(self.url, {'q': 'Algorithmics'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('COMPSCI4009', ids)

    def test_search_by_code(self):
        response = self.client.get(self.url, {'q': 'COMPSCI'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('COMPSCI4009', ids)
        self.assertIn('COMPSCI2024', ids)
        self.assertNotIn('MATH1017', ids)

    def test_search_returns_empty_for_no_match(self):
        response = self.client.get(self.url, {'q': 'Zoology'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['results']), 0)

    def test_search_is_case_insensitive(self):
        response = self.client.get(self.url, {'q': 'algorithmics'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('COMPSCI4009', ids)

    def test_empty_query_returns_results(self):
        response = self.client.get(self.url, {'q': ''})
        self.assertEqual(response.status_code, 200)

    def test_filter_by_level(self):
        response = self.client.get(self.url, {'q': '', 'level': '4'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('COMPSCI4009', ids)
        self.assertNotIn('COMPSCI2024', ids)

    def test_filter_by_school(self):
        response = self.client.get(self.url, {'q': '', 'school': self.school2.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('MATH1017', ids)
        self.assertNotIn('COMPSCI4009', ids)

    def test_filter_by_credits(self):
        self.module3.credits = 10
        self.module3.save()
        response = self.client.get(self.url, {'q': '', 'credits': '10'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('MATH1017', ids)
        self.assertNotIn('COMPSCI4009', ids)

    def test_combined_filters(self):
        response = self.client.get(self.url, {'q': '', 'level': '2', 'school': self.school.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        ids = [r['id'] for r in data['results']]
        self.assertIn('COMPSCI2024', ids)
        self.assertNotIn('COMPSCI4009', ids)
        self.assertNotIn('MATH1017', ids)


class TestBrowseModules(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('modules:browse_modules')

        self.school = School.objects.create(name='School of Computing Science')

        self.module1 = Module.objects.create(
            id='COMPSCI4009', name='Algorithmics', school=self.school, level=4, credits=20
        )
        self.module2 = Module.objects.create(
            id='COMPSCI2024', name='Web App Development', school=self.school, level=2, credits=20
        )

    def tearDown(self):
        Module.objects.all().delete()
        School.objects.all().delete()

    def test_browse_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_search_filter(self):
        response = self.client.get(self.url, {'q': 'Algorithmics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'COMPSCI4009')
        self.assertNotContains(response, 'COMPSCI2024')

    def test_level_filter(self):
        response = self.client.get(self.url, {'level': '4'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'COMPSCI4009')
        self.assertNotContains(response, 'COMPSCI2024')

    def test_no_results(self):
        response = self.client.get(self.url, {'q': 'Zoology'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No modules available.')

class TestModuleInteractions(TestCase):
    def setUp(self):
        self.client = Client()
        self.school = School.objects.create(name='School of Computing Science')
        self.module = Module.objects.create(
            id='COMPSCI1001', name='Programming', school=self.school, level=1, credits=20
        )

        self.user = User.objects.create_user(
            username='teststudent', email='student@test.com', password='pass123', role='student'
        )
        from modules.models import Degree
        self.degree = Degree.objects.create(code='G400', name='Computing Science')
        self.student = Student.objects.create(
            user=self.user, degree=self.degree, graduation_year=2026
        )

    def test_toggle_subscribe_module_redirect(self):
        """Test subscribing to a module via standard HTTP redirect"""
        self.client.login(username='teststudent', password='pass123')
        url = reverse('modules:toggle_subscribe', args=[self.module.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(StudentModule.objects.filter(student=self.student, module=self.module).exists())

        response = self.client.get(url)
        self.assertFalse(StudentModule.objects.filter(student=self.student, module=self.module).exists())

    def test_toggle_subscribe_module_ajax(self):
        """Test subscribing via AJAX returns correct JSON"""
        self.client.login(username='teststudent', password='pass123')
        url = reverse('modules:toggle_subscribe', args=[self.module.id])

        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['is_subscribed'])

        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['is_subscribed'])

    def test_toggle_favourite_module_ajax(self):
        """Test favouriting a module via AJAX"""
        self.client.login(username='teststudent', password='pass123')
        url = reverse('modules:toggle_favourite', args=[self.module.id])

        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(response.json()['is_favourited'])
        self.assertTrue(PinnedModule.objects.filter(student=self.student, module=self.module).exists())

    def test_non_student_cannot_subscribe_or_favourite(self):
        """Ensure moderators/admins get a 403 error if they try to subscribe"""
        mod_user = User.objects.create_user(
            username='mod', email='mod@test.com', password='pass', role='moderator'
        )
        self.client.login(username='mod', password='pass')

        sub_url = reverse('modules:toggle_subscribe', args=[self.module.id])
        response = self.client.get(sub_url)
        self.assertEqual(response.status_code, 403)


class TestModuleDetail(TestCase):
    def setUp(self):
        self.client = Client()
        self.school = School.objects.create(name='School of Computing Science')
        self.module = Module.objects.create(
            id='COMPSCI1001', name='Programming', school=self.school, level=1, credits=20
        )
        self.url = reverse('modules:module_detail', args=[self.module.id])

    def test_module_detail_loads_for_anonymous_user(self):
        """Unauthenticated users should still be able to view the module details"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['is_subscribed'])
        self.assertFalse(response.context['is_favourited'])

    def test_module_detail_context_for_subscribed_student(self):
        """Ensure context variables are correct when a student views a subscribed module"""
        user = User.objects.create_user(username='stu', password='123', role='student')
        from modules.models import Degree
        degree = Degree.objects.create(code='G400', name='Computing Science')
        student = Student.objects.create(user=user, degree=degree, graduation_year=2026)

        StudentModule.objects.create(student=student, module=self.module)
        PinnedModule.objects.create(student=student, module=self.module)

        self.client.login(username='stu', password='123')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_subscribed'])
        self.assertTrue(response.context['is_favourited'])