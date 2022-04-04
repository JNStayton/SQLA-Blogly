from unittest import TestCase
from app import app
from models import db, User, Post, Tag, PostTag

#User test dadtabase and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserTestCase(TestCase):
    """Tests for model for User"""

    def setUp(self):
        """Clean up any existing users."""
        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_repr(self):
        """Tests that the repr method returns the name"""
        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        self.assertEquals(user.__repr__(), '<Name: Testy McTesterson>')
    
    def test_get_full_name(self):
        """Tests that the get_full_name method returns the first_name and last_name"""
        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        self.assertEquals(user.get_full_name(), 'Testy McTesterson')
    

class PostTestCase(TestCase):
    """Tests for model for User"""

    def setUp(self):
        """Clean up any existing users."""
        Post.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_get_full_name(self):
        post = Post(title='Test', content='Test test test', user_id=1)

        self.assertEquals(post.user_id, 1)
        self.assertEqual(post.title, 'Test')
        self.assertEqual(post.content, 'Test test test')


class TagTestCase(TestCase):
    """Tests for model for User"""

    def setUp(self):
        """Clean up any existing users."""
        Tag.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_get_full_name(self):
        tag = Tag(tag_name='test')

        self.assertEquals(tag.tag_name, 'test')
