import unittest
from flask import current_app
from app import create_app
import os

from app.services.security import PasslibSecurity, WerkzeugSecurity
from app.services.security_manager import SecurityManager

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.PASSWORD = "#Eliel12345"

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_security_standard(self):
        security = SecurityManager(WerkzeugSecurity())
        password_encrypted = security.encrypt_password(self.PASSWORD)
        self.assertTrue(security.check_password(password_encrypted, self.PASSWORD))

    def test_security_passlib(self):
        security = SecurityManager(PasslibSecurity())
        password_encrypted = security.encrypt_password(self.PASSWORD)
        self.assertTrue(security.check_password(password_encrypted, self.PASSWORD))

if __name__ == '__main__':
    unittest.main()