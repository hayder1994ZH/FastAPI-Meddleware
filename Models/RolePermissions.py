from pydantic import BaseModel
from typing import Optional, List
from Models.User import User
from datetime import datetime

from config.moduls import RolePermissions

class Role(BaseModel):
    id:int
    name:str
    created_at:Optional[datetime] = datetime.utcnow()
    updated_at:Optional[datetime] = datetime.utcnow()
    class Config:
        orm_mode = True

class CreateRole(BaseModel):
    name:str

class Permission(BaseModel):
    id:int
    name:str
    created_at:Optional[datetime] = datetime.utcnow()
    updated_at:Optional[datetime] = datetime.utcnow()
    class Config:
        orm_mode = True
        
class createPermission(BaseModel):
    name:str

class AssignUserRoles(BaseModel):
    user_id:int
    role_id:int

class createRolePermissions(BaseModel):
    role_id:int
    permissions:List = []

class RolePermissions(BaseModel):
    role_is:int
    permission_is:int
    permission:Permission
    class Config:
        orm_mode = True

class GetRolePermissions(BaseModel):
    id:int
    name:str
    Permissions:List[RolePermissions]
    class Config:
        orm_mode = True

class RoleSchema(GetRolePermissions):
    authors: List[Permission]