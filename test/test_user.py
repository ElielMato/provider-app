import unittest
from flask import current_app
from app import create_app
import os
from app.models import User
from app import db
from app.services import UserServices
from app.services import SecurityManager
user_service = UserServices()

class UserTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user(self):
        user = self.__new_user()
        self.assertIsNotNone(user)
        self.assertEqual(user.firstname, "Eliel")
        self.assertEqual(user.lastname, "Mato")
        self.assertEqual(user.email, "elielmato360@gmail.com")
        self.assertEqual(user.password, "#Eliel12345")

    def test_compare_user(self):
        user = self.__new_user()
        user1 = self.__new_user()
        self.assertEqual(user, user1)

    def test_save(self):
        user = self.__new_user()
        user_save = user_service.save(user)
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)

    def test_delete(self):
        user = self.__new_user()
        user_save = user_service.save(user)
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)
        user_delete = user_service.delete(user_save)
        self.assertIsNone(user_delete)

    def test_find(self):
        user = self.__new_user()
        user_save = user_service.save(user)
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)
        user_find = user_service.find(1)
        self.assertIsNotNone(user_find)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)

    def test_find_all(self):
        user = self.__new_user()
        user1 = self.__new_user()
        user1.email = "eliel@gmail.com"
        user1.phone = "138741774"
        user_save = user_service.save(user)
        user_service.save(user1)
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)
        users = user_service.find_all()
        self.assertIsNotNone(users)
        self.assertGreater(len(users), 1)
        
    def test_find_by(self):
        user = self.__new_user()
        user_save = user_service.save(user)
        self.assertIsNotNone(user_save)
        self.assertIsNotNone(user_save.id)
        self.assertGreater(user_save.id, 0)
        user_find = user_service.find_by(email = "elielmato360@gmail.com")
        self.assertIsNotNone(user_find)

    def test_update(self):
        user = self.__new_user()
        user_save = user_service.save(user)
        user_save.email = "test@gmail.com"
        user_save_update = user_service.save(user)
        self.assertEqual(user_save_update.email, "test@gmail.com")
        self.assertEqual(user_save.email, user_save_update.email)
        self.assertEqual(user.email, user_save_update.email)

    def __new_user(self):
        user = User()
        user.firstname = "Eliel"
        user.lastname = "Mato"
        user.email = "elielmato360@gmail.com"
        user.password = "#Eliel12345"
        user.phone = "31334242"
        user.address = "wdjsdi3242"
        user.country = "argentina"
        user.state = "mendoza"
        user.zip_code = "5600"
        return user

if __name__ == '__main__':
    unittest.main()