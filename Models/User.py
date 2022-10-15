from datetime import datetime
from typing import Optional, List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, status
from config.moduls import Role, RolePermissions

class User(BaseModel):
    username :str
    email :str
    phone :str
    address :Optional[str] = None
    created_at :Optional[datetime]  = datetime.utcnow()
    updated_at :Optional[datetime]  = datetime.utcnow()
    roles:Optional[List] = []
    id :str
    class Config:
        orm_mode = True

class Create(BaseModel):
    username :str
    password :str
    email :str
    phone :str
    address :Optional[str] = None

class Update(BaseModel):
    username :Optional[str]
    password :Optional[str]
    email :Optional[str]
    phone :Optional[str]
    address :Optional[str]  = None