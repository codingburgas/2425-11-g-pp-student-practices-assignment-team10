import unittest
from flaskProject import create_app, db
from flaskProject.auth.models import User


class AccessControlTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()
        self.client = self.app.test_client()

        # Create student user
        user = User(username='student1', email='s1@test.com', role='student')
        user.set_password('pass')
        db.session.add(user)
        db.session.commit()

        self.client.post('/auth/login', data={
            'username': 'student1',
            'password': 'pass'
        }, follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_student_cannot_access_teacher_survey(self):
        res = self.client.get('/survey/teacher', follow_redirects=True)
        self.assertIn(b'Only teachers can access this survey', res.data)

    def test_student_cannot_access_admin(self):
        res = self.client.get('/admin/users', follow_redirects=True)
        self.assertIn(b'Unauthorized', res.data)


if __name__ == '__main__':
    unittest.main()
