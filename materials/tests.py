import json
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import School, Module, Degree, StudentModule
from materials.models import (
    StudyMaterial, FlashcardSet, Flashcard, Quiz,
    QuizQuestion, QuizAnswer, SavedMaterial, Upvote
)


class MaterialTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.school = School.objects.create(name='School of Science')
        self.degree = Degree.objects.create(
            code='G400',
            name='Computer Science'
        )
        self.degree.schools.add(self.school)

        self.user = User.objects.create_user(username='student1', password='pass', role='student')
        self.student = Student.objects.create(user=self.user, degree=self.degree, graduation_year=2026)

        self.module = Module.objects.create(
            id='BIO101',
            name='Biology 101',
            school=self.school,
            level=1,
            credits=20
        )

        StudentModule.objects.create(student=self.student, module=self.module)
        self.client.login(username='student1', password='pass')

    def test_create_flashcard_set(self):
        url = reverse('materials:api_create_flashcard')
        payload = {
            "title": "Cells",
            "module_id": self.module.id,
            "is_published": True,
            "cards": [
                {"front": "Nucleus", "back": "Control center of cell"},
                {"front": "Mitochondria", "back": "Powerhouse of cell"}
            ]
        }
        response = self.client.post(url, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(StudyMaterial.objects.filter(title='Cells', owner=self.student).exists())
        self.assertEqual(FlashcardSet.objects.count(), 1)
        self.assertEqual(Flashcard.objects.count(), 2)

    def test_create_quiz(self):
        url = reverse('materials:api_create_quiz')
        payload = {
            "title": "Biology Quiz",
            "module_id": self.module.id,
            "is_published": True,
            "questions": [
                {
                    "question_text": "What is the powerhouse of the cell?",
                    "question_type": "single",
                    "answers": [
                        {"answer_text": "Nucleus", "is_correct": False},
                        {"answer_text": "Mitochondria", "is_correct": True}
                    ]
                }
            ]
        }
        response = self.client.post(url, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(StudyMaterial.objects.filter(title='Biology Quiz', owner=self.student).exists())
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(QuizQuestion.objects.count(), 1)
        self.assertEqual(QuizAnswer.objects.count(), 2)

    def test_view_flashcard(self):
        material = StudyMaterial.objects.create(title='Test Flashcard', material_type='flashcard', owner=self.student,
                                                module=self.module, is_published=True)
        flashcard_set = FlashcardSet.objects.create(study_material=material)
        Flashcard.objects.create(flashcard_set=flashcard_set, front='Q1', back='A1', order=1)
        url = reverse('materials:view_flashcard', args=[material.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Q1')

    def test_view_quiz(self):
        material = StudyMaterial.objects.create(title='Test Quiz', material_type='quiz', owner=self.student,
                                                module=self.module, is_published=True)
        quiz = Quiz.objects.create(study_material=material)
        question = QuizQuestion.objects.create(quiz=quiz, question_text='Q1', question_type='single', order=1)
        QuizAnswer.objects.create(question=question, answer_text='A1', is_correct=True, order=1)
        url = reverse('materials:view_quiz', args=[material.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Q1')
        self.assertContains(response, 'A1')

    def test_toggle_save_material(self):
        material = StudyMaterial.objects.create(title='Saved Material', material_type='flashcard', owner=self.student,
                                                module=self.module, is_published=True)

        other_client = Client()
        other_user = User.objects.create_user(username='student2', password='pass', role='student')
        other_student = Student.objects.create(user=other_user, degree=self.degree, graduation_year=2026)
        other_client.login(username='student2', password='pass')

        url = reverse('materials:toggle_save_material', args=[material.id])

        other_client.get(url)
        self.assertTrue(SavedMaterial.objects.filter(student=other_student, study_material=material).exists())

        other_client.get(url)
        self.assertFalse(SavedMaterial.objects.filter(student=other_student, study_material=material).exists())

    def test_toggle_upvote(self):
        material = StudyMaterial.objects.create(title='Upvote Material', material_type='flashcard', owner=self.student,
                                                module=self.module, is_published=True)

        other_client = Client()
        other_user = User.objects.create_user(username='student3', password='pass', role='student')
        other_student = Student.objects.create(user=other_user, degree=self.degree, graduation_year=2026)
        other_client.login(username='student3', password='pass')

        url = reverse('materials:toggle_upvote', args=[material.id])

        other_client.get(url)
        self.assertTrue(Upvote.objects.filter(student=other_student, study_material=material).exists())

        other_client.get(url)
        self.assertFalse(Upvote.objects.filter(student=other_student, study_material=material).exists())