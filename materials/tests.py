import json
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Student
from modules.models import School, Degree, Module, StudentModule
from materials.models import (
    StudyMaterial, FlashcardSet, Flashcard,
    Quiz, QuizQuestion, QuizAnswer
)

class MaterialFilterViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.school = School.objects.create(name="School of Computing Science")
        self.degree = Degree.objects.create(code="G400", name="Computing Science", degree_type="BSc")

        self.user = User.objects.create_user(username="testuser", password="password123", role="student")
        self.student = Student.objects.create(user=self.user, degree=self.degree, graduation_year=2026)

        self.module1 = Module.objects.create(id="COMP1001", name="Programming 1", school=self.school, level=1, credits=20)
        self.module2 = Module.objects.create(id="COMP1002", name="Systems 1", school=self.school, level=1, credits=20)

        self.mat1 = StudyMaterial.objects.create(
            title="Python Basics Quiz", material_type="quiz", is_published=True,
            owner=self.student, module=self.module1
        )

        self.mat2 = StudyMaterial.objects.create(
            title="Python OOP Cards", material_type="flashcard", is_published=True,
            owner=self.student, module=self.module1
        )

        self.mat3 = StudyMaterial.objects.create(
            title="Hardware Quiz", material_type="quiz", is_published=True,
            owner=self.student, module=self.module2
        )

        self.mat4_unpublished = StudyMaterial.objects.create(
            title="Secret Draft Quiz", material_type="quiz", is_published=False,
            owner=self.student, module=self.module1
        )

    def test_filter_no_params_returns_only_published(self):
        response = self.client.get(reverse('materials:filter_materials'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 3)

    def test_filter_by_type(self):
        response = self.client.get(reverse('materials:filter_materials'), {'type': 'quiz'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        for item in data['results']:
            self.assertEqual(item['type'], 'Quiz')

    def test_filter_by_module(self):
        response = self.client.get(reverse('materials:filter_materials'), {'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 2)
        for item in data['results']:
            self.assertEqual(item['module_id'], 'COMP1001')

    def test_filter_by_both_type_and_module(self):
        response = self.client.get(reverse('materials:filter_materials'), {'type': 'flashcard', 'module': 'COMP1001'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['total_count'], 1)
        self.assertEqual(data['results'][0]['title'], "Python OOP Cards")


class MaterialCreationAPITests(TestCase):
    def setUp(self):
        self.client = Client()

        self.school = School.objects.create(name="School of Computing Science")
        self.degree = Degree.objects.create(code="G400", name="Computing Science", degree_type="BSc")

        self.user = User.objects.create_user(username="testuser", password="password123", role="student")
        self.student = Student.objects.create(user=self.user, degree=self.degree, graduation_year=2026)

        self.module = Module.objects.create(id="COMP1001", name="Programming 1", school=self.school, level=1, credits=20)

        self.flashcard_url = reverse('materials:api_create_flashcard')
        self.quiz_url = reverse('materials:api_create_quiz')

    def test_create_flashcard_set_success(self):
        self.client.login(username="testuser", password="password123")

        payload = {
            "title": "Advanced Python Flashcards",
            "module_id": self.module.id,
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

        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudyMaterial.objects.filter(material_type='flashcard').count(), 1)
        self.assertEqual(FlashcardSet.objects.count(), 1)
        self.assertEqual(Flashcard.objects.count(), 2)

        material = StudyMaterial.objects.get(title="Advanced Python Flashcards")
        self.assertEqual(material.owner, self.student)
        self.assertEqual(material.module_id, self.module.id)
        self.assertTrue(material.is_published)

    def test_create_quiz_success(self):
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

        self.assertEqual(response.status_code, 201)
        self.assertEqual(StudyMaterial.objects.filter(material_type='quiz').count(), 1)
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(QuizQuestion.objects.count(), 1)
        self.assertEqual(QuizAnswer.objects.count(), 2)

    def test_api_access_unauthenticated(self):
        payload = {"title": "Malicious Entry"}

        response_fc = self.client.post(self.flashcard_url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response_fc.status_code, 302)

        response_quiz = self.client.post(self.quiz_url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response_quiz.status_code, 302)

    def test_create_flashcard_missing_payload_data(self):
        self.client.login(username="testuser", password="password123")

        payload = {"title": "Empty Flashcard Set"}

        response = self.client.post(
            self.flashcard_url,
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(StudyMaterial.objects.filter(title="Empty Flashcard Set").count(), 0)


class MaterialViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.school = School.objects.create(name="School of Computing Science")
        self.degree = Degree.objects.create(code="G400", name="Computing Science", degree_type="BSc")
        self.module = Module.objects.create(id="COMP1001", name="Programming 1", school=self.school, level=1, credits=20)

        self.user_a = User.objects.create_user(username="student_a", password="password123", role="student")
        self.student_a = Student.objects.create(user=self.user_a, degree=self.degree, graduation_year=2026)
        StudentModule.objects.create(student=self.student_a, module=self.module)

        self.user_b = User.objects.create_user(username="student_b", password="password123", role="student")
        self.student_b = Student.objects.create(user=self.user_b, degree=self.degree, graduation_year=2026)

        self.moderator = User.objects.create_user(username="mod", password="password123", role="moderator")

        self.pub_fc_mat = StudyMaterial.objects.create(
            title="Public Flashcards", material_type="flashcard", owner=self.student_a, module=self.module, is_published=True
        )
        self.pub_fc_set = FlashcardSet.objects.create(study_material=self.pub_fc_mat)
        Flashcard.objects.create(flashcard_set=self.pub_fc_set, front="Q1", back="A1", order=1)

        self.priv_quiz_mat = StudyMaterial.objects.create(
            title="Private Quiz", material_type="quiz", owner=self.student_a, module=self.module, is_published=False
        )
        self.priv_quiz = Quiz.objects.create(study_material=self.priv_quiz_mat)
        QuizQuestion.objects.create(quiz=self.priv_quiz, question_text="Is this private?", question_type="single", order=1)

    def test_browse_materials_view(self):
        """Test browsing materials for a specific module"""
        self.client.login(username="student_a", password="password123")
        url = reverse('materials:browse_materials', args=[self.module.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_subscribed'])
        self.assertIn(self.pub_fc_mat, response.context['materials'])
        self.assertNotIn(self.priv_quiz_mat, response.context['materials'])

    def test_my_resources_student_access(self):
        """Test that a student can see their own resources grouped by module"""
        self.client.login(username="student_a", password="password123")
        response = self.client.get(reverse('materials:my_resources'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_materials'], 2)
        self.assertEqual(len(response.context['modules_with_materials']), 1)
        self.assertEqual(response.context['modules_with_materials'][0]['module'], self.module)

    def test_my_resources_non_student_access(self):
        """Ensure moderators/admins get an error message when accessing my resources"""
        self.client.login(username="mod", password="password123")
        response = self.client.get(reverse('materials:my_resources'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Only students can view their resources')

    def test_create_pages_load_correctly(self):
        """Test that create pages load and contain subscribed modules in context"""
        self.client.login(username="student_a", password="password123")

        fc_response = self.client.get(reverse('materials:create_flashcard'))
        self.assertEqual(fc_response.status_code, 200)
        self.assertIn(self.module, fc_response.context['subscribed'])

        quiz_response = self.client.get(reverse('materials:create_quiz_with_module', args=[self.module.id]))
        self.assertEqual(quiz_response.status_code, 200)
        self.assertEqual(quiz_response.context['initial_module_id'], self.module.id)

    def test_view_flashcard_published(self):
        """Anyone can view a published flashcard"""
        self.client.login(username="student_b", password="password123")
        url = reverse('materials:view_flashcard', args=[self.pub_fc_mat.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['flashcard_set'], self.pub_fc_set)

    def test_view_quiz_unpublished_owner(self):
        """The owner CAN view their own unpublished quiz"""
        self.client.login(username="student_a", password="password123")
        url = reverse('materials:view_quiz', args=[self.priv_quiz_mat.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['quiz'], self.priv_quiz)

    def test_view_quiz_unpublished_other_student(self):
        """Other students CANNOT view an unpublished quiz"""
        self.client.login(username="student_b", password="password123")
        url = reverse('materials:view_quiz', args=[self.priv_quiz_mat.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'You do not have permission to view this material')