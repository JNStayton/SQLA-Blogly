from unittest import TestCase
from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

#Make flask errors be real errors rather than HTML pages with error info
app.config['TESTING'] = True

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for User"""

    def setUp(self):
        """Add sample user"""

        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.drop_all()
        db.create_all()

    def test_go_home(self):
        with app.test_client() as client:
            resp = client.get('/', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertIn('Testy McTesterson', html)

    def test_sign_up(self):
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h3>Sign Up</h3>', html)

    def test_create_user(self):
        with app.test_client() as client:
            d = {'first_name': 'Testy', 'last_name': 'McTests', 'image_url': 'https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png'}

            resp = client.post('/users/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTests', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get('/users/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTesterson', html)

    def test_save_edited_user(self):
        with app.test_client() as client:
            d = {'first_name': 'Testy', 'last_name': 'McTests', 'image_url': 'https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png'}

            resp = client.post('/users/1/edit', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTests', html)

    def test_delete_user(self):
        with app.test_client() as client:
            resp = client.post('/users/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Testy McTesterson', html)