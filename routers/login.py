from fastapi import APIRouter, Depends, Response, HTTPException, status
from config.database import engine, SessionLocal, get_db
from Controllers.AuthController import AuthController
from fastapi.security import OAuth2PasswordRequestForm
from Models.User import Create, User
from Models.Authintecation.Oauth2 import get_current_user
router = APIRouter(
    prefix="/auth",
    tags=["Authintecation"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
def loginAuth(response:Response,form_data: OAuth2PasswordRequestForm = Depends(), db:SessionLocal = Depends(get_db)):
    return AuthController().login(form_data, response)


@router.post("/registration")
def registration(response:Response,request: Create):
    return AuthController().register(request, response)

@router.get("/profile", status_code=status.HTTP_200_OK)
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user