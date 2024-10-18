from typing import List
from app.models import User
from app.repositories import UserRepository
from app.services import SecurityManager, WerkzeugSecurity

class UserServices():

    def save(self, user:User) -> User:    
        if user.id is None:
            security = SecurityManager(WerkzeugSecurity())
            user.password = security.encrypt_password(user.password)
        UserRepository.save(user)
        return user
    
    def delete(self, user:User) -> None:
        UserRepository.delete(user)

    def find(self, id: int) -> 'User':
        return UserRepository.find(id)

    def find_all(self) -> List['User']:
        return UserRepository.find_all()
    
    def find_by(self, **kwargs) -> List['User']:
        return UserRepository.find_by(**kwargs)