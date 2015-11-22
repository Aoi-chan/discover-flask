from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # Works at all?
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Login page loads?
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertIn(b'Please login', response.data)

    # Logs in with correct credentials?
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                data=dict(username='admin', password='admin'),
                follow_redirects = True)
        self.assertIn(b'You were just logged in!', response.data)

    # Login redirects with wrong credentials?
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                data=dict(username='admin', password='wrong'),
                follow_redirects = True)
        self.assertIn(b'Invalid credentials.', response.data)

    # Logs out?
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                data=dict(username='admin', password='admin'),
                follow_redirects = True)
        response = tester.get('/logout', follow_redirects = True)
        self.assertIn(b'You were just logged out!', response.data)

    # Main page requires login?
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects = True)
        self.assertIn(b'You need to login first.', response.data)

    # Logout page requires login?
    def test_logout_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects = True)
        self.assertIn(b'You need to login first.', response.data)

    # Posts show up on the main page?
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                data=dict(username='admin', password='admin'),
                follow_redirects = True)
        self.assertIn(b'I&#39;m well.', response.data)

if __name__ == '__main__':
    unittest.main()
