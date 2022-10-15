from fastapi import APIRouter, Depends, Response, status, HTTPException, Request
from Helper.Utilities import Utilities
from Middleware.RoleMiddleware import RoleMiddleware
from config.database import engine, SessionLocal, get_db
from Controllers.UserController import UserController
from Models.User import Create
from Models.User import User
from typing import List
from Models.Authintecation.Oauth2 import get_current_active_user, get_current_user

router = APIRouter(
    prefix="/api/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


#User Routes
@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
def index(take = 10, skip = 0, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-users", get_current_user)
    return  UserController().index(take, skip)

@router.post("/")
def create(response:Response,request: Create, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("store-users", get_current_user)
    return UserController().store(request, response)

@router.get("/getApiData")
def show(request: Request, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("show-user-data", get_current_user)
    return "Hello World"
