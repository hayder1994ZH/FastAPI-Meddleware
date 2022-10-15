from fastapi import APIRouter, Depends, HTTPException,Response, status, Request
from Middleware.RoleMiddleware import RoleMiddleware
from config.database import engine, SessionLocal, get_db
from Controllers.PostController import PostController
from Models.Post import Create, Post, Update
from typing import List
from Models.User import User
from Models.Post import Post
from Models.Authintecation.Oauth2 import get_current_user
from fastapi import File, UploadFile
import shutil

router = APIRouter(
    prefix="/api/post",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=List[Post])
def index(take = 10, skip = 0, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-posts", get_current_user)
    return  PostController().index(take, skip)

@router.get("/{id}", response_model=Post)
def show(id: int, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("show-posts", get_current_user)
    return  PostController().show(id)

@router.post("", status_code=status.HTTP_200_OK)
def create(response:Response, request: Create, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("store-posts", get_current_user)
    user_id = get_current_user.id
    return  PostController().create(request, response, user_id)

@router.delete("/{id}")
def delete(id: int, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("delete-posts", get_current_user)
    return  PostController().delete(id)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(id: int,  response:Response, request: Update, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("update-posts", get_current_user)
    return  PostController().updated(id, request, response)

@router.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open("images/"+file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfully uploaded {file.filename}"}