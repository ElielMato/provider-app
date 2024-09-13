from app.services.security import AbstractSecurity

class SecurityManager:

    def __init__(self, security: AbstractSecurity) -> None:
        self.__security = security

    def encrypt_password(self, password:str) -> str:
        return self.__security.encrypt_password(password)
    
    def check_password(self, password_encrypted:str, plain_password:str) -> bool:
        return self.__security.check_password(password_encrypted, plain_password)