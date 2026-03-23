import json
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import School, Degree, Module
from materials.models import (
    StudyMaterial, FlashcardSet, Flashcard,
    Quiz, QuizQuestion, QuizAnswer
)
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
        response = self.client.get(reverse('materials:filter_materials'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 3)

    def test_filter_by_type(self):
        #Test: Filtering by type=quiz should return exactly 2 quiz materials
        response = self.client.get(reverse('materials:filter_materials'), {'type': 'quiz'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        # Verify that every element in the returned list has the type 'Quiz'
        for item in data['results']:
            self.assertEqual(item['type'], 'Quiz')

    def test_filter_by_module(self):
        #Test: Filtering by module=COMP1001 should return exactly 2 materials corresponding to that module
        response = self.client.get(reverse('materials:filter_materials'), {'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        for item in data['results']:
            self.assertEqual(item['module_id'], 'COMP1001')

    def test_filter_by_both_type_and_module(self):
        #Test: Filtering by both type=flashcard and module=COMP1001 should precisely match 1 material
        response = self.client.get(reverse('materials:filter_materials'), {'type': 'flashcard', 'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 1)
        self.assertEqual(data['results'][0]['title'], "Python OOP Cards")


class MaterialCreationAPITests(TestCase):
    def setUp(self):
        """
        Set up prerequisite data for the creation APIs.
        Reusing the exact dependency structure from the existing tests.
        """
        self.client = Client()

        # 1. Create prerequisite dependency data
        self.school = School.objects.create(name="School of Computing Science")
        self.degree = Degree.objects.create(code="G400", name="Computing Science", degree_type="BSc")

        # 2. Create a user and the corresponding Student Profile
        self.user = User.objects.create_user(username="testuser", password="password123", role="student")
        self.student = Student.objects.create(user=self.user, degree=self.degree, graduation_year=2026)

        # 3. Create a test module (Note: module id is a string like "COMP1001")
        self.module = Module.objects.create(id="COMP1001", name="Programming 1", school=self.school, level=1, credits=20)

        # 4. Store the API endpoints
        self.flashcard_url = reverse('materials:api_create_flashcard')
        self.quiz_url = reverse('materials:api_create_quiz')

    def test_create_flashcard_set_success(self):
        """Test: Successfully create a Flashcard Set with valid data"""
        self.client.login(username="testuser", password="password123")

        payload = {
            "title": "Advanced Python Flashcards",
            "module_id": self.module.id,  # Using "COMP1001"
            "is_published": True,
            "cards": [
                {"front": "What are decorators?", "back": "Functions that modify other functions."},
                {"front": "What is a lambda function?", "back": "An anonymous inline function."}
            ]
        }

        response = self.client.post(
            self.flashcard_url,
            data=json.dumps(payload),
            content_type='application/json'
        )

        # Verify HTTP status code
        self.assertEqual(response.status_code, 201)

        # Verify database insertion
        self.assertEqual(StudyMaterial.objects.filter(material_type='flashcard').count(), 1)
        self.assertEqual(FlashcardSet.objects.count(), 1)
        self.assertEqual(Flashcard.objects.count(), 2)

        # Verify relationships and data integrity
        material = StudyMaterial.objects.get(title="Advanced Python Flashcards")
        self.assertEqual(material.owner, self.student)
        self.assertEqual(material.module_id, self.module.id)
        self.assertTrue(material.is_published)

    def test_create_quiz_success(self):
        """Test: Successfully create a Quiz with nested questions and answers"""
        self.client.login(username="testuser", password="password123")

        payload = {
            "title": "Midterm Prep Quiz",
            "module_id": self.module.id,
            "is_published": False,
            "questions": [
                {
                    "question_text": "What is the primary key in Django models by default?",
                    "question_type": "single",
                    "answers": [
                        {"answer_text": "uuid", "is_correct": False},
                        {"answer_text": "id (auto-incrementing integer)", "is_correct": True}
                    ]
                }
            ]
        }

        response = self.client.post(
            self.quiz_url,
            data=json.dumps(payload),
            content_type='application/json'
        )

        # Verify HTTP status code
        self.assertEqual(response.status_code, 201)

        # Verify database records
        self.assertEqual(StudyMaterial.objects.filter(material_type='quiz').count(), 1)
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(QuizQuestion.objects.count(), 1)
        self.assertEqual(QuizAnswer.objects.count(), 2)

    def test_api_access_unauthenticated(self):
        """Test: Unauthenticated users should be redirected or blocked"""
        payload = {"title": "Malicious Entry"}

        # Test Flashcard endpoint
        response_fc = self.client.post(self.flashcard_url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response_fc.status_code, 302) # @login_required triggers a 302 redirect to login page

        # Test Quiz endpoint
        response_quiz = self.client.post(self.quiz_url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response_quiz.status_code, 302)

    def test_create_flashcard_missing_payload_data(self):
        """Test: Providing incomplete JSON payload should return 400 Bad Request"""
        self.client.login(username="testuser", password="password123")

        # Missing the 'cards' array entirely
        payload = {"title": "Empty Flashcard Set"}

        response = self.client.post(
            self.flashcard_url,
            data=json.dumps(payload),
            content_type='application/json'
        )

        # Verify it was rejected by our validation logic
        self.assertEqual(response.status_code, 400)

        # Ensure no garbage data was saved to the database
        self.assertEqual(StudyMaterial.objects.filter(title="Empty Flashcard Set").count(), 0)