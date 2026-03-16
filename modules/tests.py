from django.test import TestCase, Client
from django.urls import reverse
from .models import School, Module


class TestModuleAutocomplete(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('modules:module_autocomplete')

        self.school = School.objects.create(name='School of Computing Science')

        self.module1 = Module.objects.create(
            id='COMPSCI4009', name='Algorithmics', school=self.school, level=4, credits=20
        )
        self.module2 = Module.objects.create(
            id='COMPSCI2024', name='Web App Development', school=self.school, level=2, credits=20
        )
        self.module3 = Module.objects.create(
            id='MATH1017', name='Calculus', school=self.school, level=1, credits=20
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

