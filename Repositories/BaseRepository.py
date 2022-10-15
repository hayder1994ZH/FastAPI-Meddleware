from abc import ABC, abstractmethod
from fastapi import Depends, HTTPException, Response, status
from config.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
class BaseRepository(ABC):
    db = Session(bind=engine, expire_on_commit=False)
    def __init__(self, model):
        self.model = model

    
    def getList(self, limit: int = 10, skip: int = 0):
        return  self.db.query(self.model).offset(skip).limit(limit).all()
    
    def show(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def store(self, new_blog, response):
        self.db.add(new_blog)
        self.db.commit()
        self.db.refresh(new_blog)
        response.status_code=status.HTTP_201_CREATED
        response.body = {
                    "status": True,
                    "message": f"{self.model.__class__.__name__} created successfully"
                }
        return response.body

    def updated(self, id, request, response):
        request =  request.dict()
        blog = self.db.query(self.model).filter(self.model.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"this {self.model.__class__.__name__} with id {id} not found")
        blog.update(request)
        self.db.commit()
        response.status_code=status.HTTP_200_OK
        response.body = {
                "status": True,
                "message": f"updated {self.model.__class__.__name__} successfully"
            }
        return response.body

    def delete(self, id):
        blog = self.db.query(self.model).filter(self.model.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"this {self.model.__class__.__name__} with id {id} not found")
        blog.delete(synchronize_session=False)
        self.db.commit()
        return {"Success": f"{self.model.__class__.__name__} deleted"}