from pydantic import BaseModel
from typing import Optional, List
from Models.User import User
from datetime import datetime

class Post(BaseModel):
    id:int
    title: str
    body: str
    image: str
    creator_id:Optional[int] = None
    creator: User
    created_at :Optional[datetime]  = datetime.utcnow()
    updated_at :Optional[datetime]  = datetime.utcnow()
    class Config:
        orm_mode = True

class Create(BaseModel):
    title: str
    body: str
    image: str

class Update(BaseModel):
    title: str
    body: str
    image: str
