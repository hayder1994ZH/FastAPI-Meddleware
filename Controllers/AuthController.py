from config.moduls import User
from passlib.context import CryptContext
from Repositories.AuthRepository import AuthRepository
from Models.Authintecation.Hash import hash_password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthController:
    def __init__(self, AuthRepo = AuthRepository(User)):
        self.AuthRepo = AuthRepo

    def login(self, request, response):
        return self.AuthRepo.login(request, response)

    def register(self, request, response):
        user = User(username=request.username, email=request.email, phone=request.phone, address=request.address, password=hash_password(request.password))
        return self.AuthRepo.store(user, response)