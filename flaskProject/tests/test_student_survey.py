import unittest
from flaskProject import create_app, db
from flaskProject.auth.models import User
from flaskProject.form.models import StudentSurveyResponse


class StudentSurveyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()

        user = User(username='studentx', email='sx@test.com', role='student')
        user.set_password('pass')
        db.session.add(user)
        db.session.commit()

        self.client.post('/auth/login', data={
            'username': 'studentx',
            'password': 'pass'
        }, follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_student_survey_submission(self):
        response = self.client.post('/survey/student', data={
            'favorite_subject': 'Math',
            'learning_style': 'Visual',
            'strength': 'Problem-solving',
            'future_study': 'Engineering',
            'class_behavior': 'Focused',
            'activities': 'Robotics',
            'goal': 'University'
        }, follow_redirects=True)

        self.assertIn(b'Survey submitted successfully', response.data)
        survey = StudentSurveyResponse.query.filter_by(student_id=1).first()
        self.assertIsNotNone(survey)

    def test_prevent_duplicate_submission(self):
        survey = StudentSurveyResponse(
            student_id=1,
            favorite_subject='Math',
            learning_style='Visual',
            strength='Logic',
            future_study='CS',
            class_behavior='Calm',
            activities='Chess',
            goal='AI'
        )
        db.session.add(survey)
        db.session.commit()

        response = self.client.get('/survey/student', follow_redirects=True)
        self.assertIn(b'already submitted this survey', response.data)


if __name__ == '__main__':
    unittest.main()
