import unittest
from flask import current_app
from app import create_app
import os
from app.models import User
from app import db

class UserTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        #db.drop_all()
        self.app_context.pop()

    def test_user(self):
        user = self.__new_user()
        self.assertIsNotNone(user)
        self.assertEqual(user.firstname, "Eliel")
        self.assertEqual(user.lastname, "Mato")
        self.assertEqual(user.email, "elielmato360@gmail.com")
        self.assertEqual(user.password, "12345")

    def test_compare_user(self):
        user = self.__new_user()
        user1 = self.__new_user()
        self.assertEqual(user, user1)

    def test_save(self):
        user = self.__new_user()
        user_save = user.save()
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)

    def __new_user(self):
        user = User()
        user.firstname = "Eliel"
        user.lastname = "Mato"
        user.email = "elielmato360@gmail.com"
        user.password = "12345"
        user.phone = "31334242"
        user.address = "wdjsdi3242"
        user.country = "argentina"
        user.province = "mendoza"
        user.zip_code = "5600"
        return user

if __name__ == '__main__':
    unittest.main()