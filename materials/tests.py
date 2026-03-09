from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import School, Degree, Module
from materials.models import StudyMaterial

class MaterialFilterViewTests(TestCase):
    def setUp(self):
        """
        Set up prerequisite data for the tests.
        Django creates a clean test database and runs this code before each test method.
        """
        self.client = Client()

        # 1. Create prerequisite dependency data
        self.school = School.objects.create(name="School of Computing Science")
        self.degree = Degree.objects.create(code="G400", name="Computing Science", degree_type="BSc")

        # 2. Create a user and the corresponding Student Profile
        self.user = User.objects.create_user(username="testuser", password="password123", role="student")
        self.student = Student.objects.create(user=self.user, degree=self.degree, graduation_year=2026)

        # 3. Create test modules
        self.module1 = Module.objects.create(id="COMP1001", name="Programming 1", school=self.school, level=1, credits=20)
        self.module2 = Module.objects.create(id="COMP1002", name="Systems 1", school=self.school, level=1, credits=20)

        # 4. Create study materials with various statuses
        # Material 1: Quiz for COMP1001 (Published) -> Should be retrieved
        self.mat1 = StudyMaterial.objects.create(
            title="Python Basics Quiz", material_type="quiz", is_published=True,
            owner=self.student, module=self.module1
        )

        # Material 2: Flashcard for COMP1001 (Published) -> Should be retrieved
        self.mat2 = StudyMaterial.objects.create(
            title="Python OOP Cards", material_type="flashcard", is_published=True,
            owner=self.student, module=self.module1
        )

        # Material 3: Quiz for COMP1002 (Published) -> Should be retrieved
        self.mat3 = StudyMaterial.objects.create(
            title="Hardware Quiz", material_type="quiz", is_published=True,
            owner=self.student, module=self.module2
        )

        # Material 4: Quiz for COMP1001 (Unpublished) -> Should NOT be retrieved!
        self.mat4_unpublished = StudyMaterial.objects.create(
            title="Secret Draft Quiz", material_type="quiz", is_published=False,
            owner=self.student, module=self.module1
        )

    def test_filter_no_params_returns_only_published(self):
        #Test: If no filter parameters are provided, it should return only all published materials
        response = self.client.get(reverse('filter_materials'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 3)

    def test_filter_by_type(self):
        #Test: Filtering by type=quiz should return exactly 2 quiz materials
        response = self.client.get(reverse('filter_materials'), {'type': 'quiz'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        # Verify that every element in the returned list has the type 'Quiz'
        for item in data['results']:
            self.assertEqual(item['type'], 'Quiz')

    def test_filter_by_module(self):
        #Test: Filtering by module=COMP1001 should return exactly 2 materials corresponding to that module
        response = self.client.get(reverse('filter_materials'), {'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        for item in data['results']:
            self.assertEqual(item['module_id'], 'COMP1001')

    def test_filter_by_both_type_and_module(self):
        #Test: Filtering by both type=flashcard and module=COMP1001 should precisely match 1 material
        response = self.client.get(reverse('filter_materials'), {'type': 'flashcard', 'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 1)
        self.assertEqual(data['results'][0]['title'], "Python OOP Cards")
