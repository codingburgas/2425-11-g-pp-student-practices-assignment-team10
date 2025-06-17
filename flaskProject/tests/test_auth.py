import unittest
from flaskProject import create_app, db
from flaskProject.auth.models import User


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def register_user(self, username, email, password, role="student"):
        return self.client.post('/auth/register', data={
            'username': username,
            'email': email,
            'password': password,
            'confirm': password,
            'role': role,
            'submit': True
        }, follow_redirects=True)

    def login_user(self, username, password):
        return self.client.post('/auth/login', data={
            'username': username,
            'password': password,
            'submit': True
        }, follow_redirects=True)

    def logout_user(self):
        return self.client.get('/auth/logout', follow_redirects=True)

    def test_register(self):
        res = self.register_user("newuser", "new@example.com", "password123")
        self.assertIn(b'Registration successful', res.data)
        user = User.query.filter_by(username="newuser").first()
        self.assertIsNotNone(user)

    def test_login_logout(self):
        # First register the user
        self.register_user("testuser", "test@example.com", "secret")

        # Login
        res = self.login_user("testuser", "secret")
        self.assertIn(b'Profile', res.data)

        # Logout
        res = self.logout_user()
        self.assertIn(b'Home', res.data)

    def test_invalid_login(self):
        res = self.login_user("wrong", "wrongpass")
        self.assertIn(b'Invalid username or password', res.data)


if __name__ == '__main__':
    unittest.main()
