from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from Models.Authintecation.JWTtoken import verify_token
from  jose import JWTError, jwt
from Models.Authintecation.JWTtoken import SECRET_KEY, ALGORITHM
from Models.Authintecation.Login import TokenData
from Models.User import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def check_authorized_user(roleName, methodName, current_user: User = Depends(get_current_user)):
    if roleName == 'admin':
        raise HTTPException(status_code=400, detail= methodName)
    return current_user