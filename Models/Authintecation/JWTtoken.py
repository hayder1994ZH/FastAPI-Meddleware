
from datetime import datetime, timedelta 
from  jose import JWTError, jwt
from typing import Optional, Union
from Models.Authintecation.Login import TokenData
from fastapi import APIRouter, Depends, Response, status
from config.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, joinedload
from config.moduls import User, UserRoles, Role, RolePermissions, Permission
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93fdfg7099f6f0f4caa6c456f63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
db = Session(bind=engine, expire_on_commit=False)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=3600)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_auth_user(username):
    return db.query(User).filter(User.username == username).first()

def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username = username)
    except JWTError:
        raise credentials_exception
    user = get_auth_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    userAuthInfo =  db.query(User).filter(User.id == user.id).options(
    joinedload(User.roles).joinedload(UserRoles.role)).first()
    userPermissions = []
    for role in userAuthInfo.roles:
        role.permissions = db.query(RolePermissions).filter(RolePermissions.role_id == role.role_id).options(
        joinedload(RolePermissions.permission)).all()
        for permission in role.permissions:
            userPermissions.append(permission.permission.name) 
    return userPermissions
        