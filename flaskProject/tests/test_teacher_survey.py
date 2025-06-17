import unittest
from flaskProject import create_app, db
from flaskProject.auth.models import User
from flaskProject.form.models import TeacherSurveyResponse


class TeacherSurveyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()

        teacher = User(username='teach1', email='teach1@example.com', role='teacher')
        teacher.set_password('testpass')
        db.session.add(teacher)
        db.session.commit()

        self.client.post('/auth/login', data={
            'username': 'teach1',
            'password': 'testpass'
        }, follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_teacher_survey_submission(self):
        response = self.client.post('/survey/teacher', data={
            'student_name': 'John Doe',
            'observations': 'Strong analytical skills',
            'improvement': 'Public speaking',
            'recommendation': 'Encourage group work'
        }, follow_redirects=True)

        self.assertIn(b'Survey submitted successfully', response.data)
        survey = TeacherSurveyResponse.query.first()
        self.assertIsNotNone(survey)
        self.assertEqual(survey.student_name, 'John Doe')


if __name__ == '__main__':
    unittest.main()
