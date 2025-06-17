import unittest
from flaskProject import create_app, db
from flaskProject.auth.models import User


class ProfileTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()
        self.client = self.app.test_client()

        # Create and login user
        user = User(username='user1', email='user1@test.com', role='student')
        user.set_password('pass123')
        db.session.add(user)
        db.session.commit()

        self.client.post('/auth/login', data={
            'username': 'user1',
            'password': 'pass123'
        }, follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_view_profile(self):
        res = self.client.get('/profile')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'user1', res.data)

    def test_edit_profile(self):
        res = self.client.post('/edit-profile', data={
            'username': 'newuser1',
            'email': 'newemail@test.com',
            'password': '',
            'confirm': '',
            'submit': True
        }, follow_redirects=True)
        self.assertIn(b'Profile updated successfully', res.data)

        user = User.query.filter_by(username='newuser1').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'newemail@test.com')

    def test_duplicate_username_email(self):
        # Add another user
        user2 = User(username='existing', email='existing@test.com', role='teacher')
        user2.set_password('secret')
        db.session.add(user2)
        db.session.commit()

        res = self.client.post('/edit-profile', data={
            'username': 'existing',
            'email': 'existing@test.com',
            'password': '',
            'confirm': '',
            'submit': True
        }, follow_redirects=True)

        self.assertIn(b'Username already taken', res.data)


if __name__ == '__main__':
    unittest.main()
