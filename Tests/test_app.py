from unittest import TestCase
from app import app
from models import db, User, Post, Tag, PostTag

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
        """Tests that / redirects to /users"""
        with app.test_client() as client:
            resp = client.get('/', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertIn('Testy McTesterson', html)

    def test_sign_up(self):
        """Tests that sign up page shows on /users/new"""
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h3>Sign Up</h3>', html)

    def test_create_user(self):
        """Tests that created user is saved to db"""
        with app.test_client() as client:
            d = {'first_name': 'Testy', 'last_name': 'McTests', 'image_url': 'https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png'}

            resp = client.post('/users/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTests', html)

    def test_show_user(self):
        """Tests that user details show up on user page"""
        with app.test_client() as client:
            resp = client.get('/users/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTesterson', html)

    def test_save_edited_user(self):
        """Tests that edited user details are saved to db"""
        with app.test_client() as client:
            d = {'first_name': 'Testy', 'last_name': 'McTests', 'image_url': 'https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png'}

            resp = client.post('/users/1/edit', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Testy McTests', html)

    def test_delete_user(self):
        """Tests that user is deleted from db"""
        with app.test_client() as client:
            resp = client.post('/users/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Testy McTesterson', html)

class PostViewsTestCase(TestCase):
    """Tests for views for Post"""

    def setUp(self):
        """Add sample post"""
        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        db.session.add(user)
        db.session.commit()

        post = Post(title='Test', content='Test test test', user_id=1, )

        db.session.add(post)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.drop_all()
        db.create_all()

    def test_show_post(self):
        """Test the show route for posts"""
        with app.test_client() as client:
            resp = client.get('/posts/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test', html)

    def test_create_post(self):
        """Test that submitted post data saved to db"""
        with app.test_client() as client:
            d = {'title': 'Test', 'content': 'Test', 'user_id': 1}

            resp = client.post('/users/1/posts/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test', html)
    
    def test_delete_post(self):
        """Tests that post is deleted from db"""
        with app.test_client() as client:
            resp = client.post('/posts/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Test test test', html)


class TagViewsTestCase(TestCase):
    """Tests for views for Post"""

    def setUp(self):
        """Add sample post"""
        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        db.session.add(user)
        db.session.commit()

        post = Post(title='Test', content='Test test test', user_id=1, )

        db.session.add(post)
        db.session.commit()

        tag = Tag(tag_name='tessst')

        db.session.add(tag)
        db.session.commit()

        post.categories.append(PostTag(post_id=1, tag_id=1))

        db.session.add(post)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.drop_all()
        db.create_all()

    def test_show_tag(self):
        """Test the show route for tag"""
        with app.test_client() as client:
            resp = client.get('/tags/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('tessst', html)

    def test_create_tag(self):
        """Test that submitted tag data saved to db"""
        with app.test_client() as client:
            d = {'tag_name': 'oyyy'}

            resp = client.post('/tags/new', data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('oyyy', html)
    
    def test_delete_tag(self):
        """Tests that tag is deleted from db"""
        with app.test_client() as client:
            resp = client.post('/tags/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('tessst', html)