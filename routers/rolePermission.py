from fastapi import APIRouter, Depends, Response, status, HTTPException
from Helper.Utilities import Utilities
from config.database import engine, SessionLocal, get_db
from Controllers.RolePermissionController import RolePermissionController
from Middleware.RoleMiddleware import RoleMiddleware
from Models.RolePermissions import CreateRole, GetRolePermissions, Role, createPermission, Permission, createRolePermissions, AssignUserRoles
from Models.User import User
from typing import List
from Models.Authintecation.Oauth2 import get_current_active_user, get_current_user

router = APIRouter(
    prefix="/api/authorize",
    responses={404: {"description": "Not found"}},
)


#Roles Routes
@router.get("/role", status_code=status.HTTP_200_OK, tags=["Role"])
def index(take = 10, skip = 0, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-roles", get_current_user)
    return  RolePermissionController().getListRole(take, skip)

@router.post("/role", tags=["Role"])
def create(response:Response,request: CreateRole, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("store-roles", get_current_user)
    return RolePermissionController().createRole(request, response)

#Permissions Routes
@router.get("/permission", status_code=status.HTTP_200_OK, tags=["Permission"])
def index(take = 10, skip = 0, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-permissions", get_current_user)
    return  RolePermissionController().getPermission(take, skip)

@router.post("/permission", tags=["Permission"])
def create(response:Response,request: createPermission, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("store-permissions", get_current_user)
    return RolePermissionController().createPermission(request, response)

@router.post("/assign/permission/to/role", tags=["RolePermissions"])
def create(response:Response,request: createRolePermissions, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("assign-permissions-to-role", get_current_user)
    return RolePermissionController().createRolePermission(request, response)

@router.post("/assign/roles/to/user", tags=["Role"])
def create(response:Response,request: AssignUserRoles, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("assign-roles-to-user", get_current_user)
    return RolePermissionController().assignUserRoles(request, response)

@router.get("/role/permissions/{id}", status_code=status.HTTP_200_OK, tags=["Role"])
def index(id: int, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-role-permissions", get_current_user)
    return  RolePermissionController().getRolePermission(id)

@router.get("/roles/user/{id}", status_code=status.HTTP_200_OK, tags=["Role"])
def index(id: int, get_current_user: User = Depends(get_current_user)):
    RoleMiddleware.permissions("get-user-roles", get_current_user)
    return  RolePermissionController().getUserRole(id)