from unittest import TestCase
from app import app
from models import db, User

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
        user = User(first_name='Testy', last_name='McTesterson', image_url='https://www.pngitem.com/pimgs/m/507-5072130_cliparts-for-free-english-test-clipart-hd-png.png')

        self.assertEquals(user.__repr__(), '<Name: Testy McTesterson>')