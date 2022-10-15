from config.moduls import User
from Repositories.UserRepository import UserRepository
from Models.Authintecation.Hash import hash_password  # <--- import the hash_password function

class UserController:
    def __init__(self, UserRepo = UserRepository(User)):
        self.UserRepo = UserRepo

    def index(self, take, skip):
        return self.UserRepo.getList()

    def store(self, request, response):
        user = User(username=request.username, email=request.email, phone=request.phone, address=request.address, password=hash_password(request.password))
        return self.UserRepo.store(user, response)