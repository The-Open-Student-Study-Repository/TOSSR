import json  # Essential for JSON payloads
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import Module, Degree, StudentModule, School
from materials.models import StudyMaterial, FlashcardSet, Flashcard, Quiz, QuizQuestion, QuizAnswer, SavedMaterial, \
    Upvote


class MaterialTests(TestCase):
    def setUp(self):
        self.client = Client()

        # 1. Create School first (Required by Module)
        self.school = School.objects.create(name='School of Computing Science')

        # 2. Create Degree with a code (Primary Key)
        self.degree = Degree.objects.create(
            code='G400',
            name='Computing Science',
            degree_type='BSc (Hons)'
        )
        self.degree.schools.add(self.school)  # Optional, but good for data integrity

        # 3. Create Module with all required fields
        # Note: id is the primary key and must be a string (max 16)
        self.module = Module.objects.create(
            id='COMPSCI2001',
            name='Biology 101',
            school=self.school,
            level=2,
            credits=20
        )

        # 4. Create User and Student
        self.user = User.objects.create_user(
            username='student1',
            password='pass',
            role='student'
        )
        self.student = Student.objects.create(
            user=self.user,
            degree=self.degree,
            graduation_year=2026
        )

        # 5. Subscribe student to module
        StudentModule.objects.create(student=self.student, module=self.module)

        self.client.login(username='student1', password='pass')

    def test_create_flashcard_set(self):
        url = reverse('materials:api_create_flashcard')
        payload = {
            "title": "Cells",
            "module_id": self.module.id,
            "is_published": True,
            "cards": [
                {"front": "Nucleus", "back": "Control center"},
                {"front": "Mitochondria", "back": "Powerhouse"}
            ]
        }
        # FIX: Must wrap payload in json.dumps()
        response = self.client.post(url, json.dumps(payload), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(StudyMaterial.objects.filter(title='Cells', owner=self.student).exists())

    def test_create_quiz(self):
        url = reverse('materials:api_create_quiz')
        payload = {
            "title": "Biology Quiz",
            "module_id": self.module.id,
            "is_published": True,
            "questions": [
                {
                    "question_text": "Powerhouse?",
                    "question_type": "single",
                    "answers": [
                        {"answer_text": "Mito", "is_correct": True}
                    ]
                }
            ]
        }
        # FIX: json.dumps() here as well
        response = self.client.post(url, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_toggle_save_material(self):
        material = StudyMaterial.objects.create(
            title='Saved Material', material_type='flashcard',
            owner=self.student, module=self.module, is_published=True
        )

        # FIX: Create a separate client for the 'other' user to avoid session bleeding
        other_client = Client()
        other_user = User.objects.create_user(username='student2', password='pass', role='student')
        other_student = Student.objects.create(user=other_user, degree=self.degree, graduation_year=2026)
        other_client.login(username='student2', password='pass')

        url = reverse('materials:toggle_save_material', args=[material.id])

        # First toggle: Save
        response = other_client.get(url)
        self.assertTrue(SavedMaterial.objects.filter(student=other_student, study_material=material).exists())

        # Second toggle: Unsave
        response = other_client.get(url)
        self.assertFalse(SavedMaterial.objects.filter(student=other_student, study_material=material).exists())

    # Apply the 'other_client' fix to test_toggle_upvote as well