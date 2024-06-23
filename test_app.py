import unittest
from app import app, db
from app.models import Character

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_character(self):
        with app.app_context():
            # Ujistíme se, že databáze je prázdná před testem
            db.session.query(Character).delete()
            db.session.commit()

            character = Character(name='Test', character_class='bojovník')
            db.session.add(character)
            db.session.commit()
            self.assertEqual(Character.query.count(), 1)

    def test_index_redirect(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
