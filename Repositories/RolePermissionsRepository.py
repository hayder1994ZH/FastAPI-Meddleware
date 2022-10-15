
from Models.RolePermissions import RoleSchema
from config.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from config.moduls import Role, Permission, RolePermissions, User, UserRoles
from fastapi import Depends, HTTPException, Response, status
from config.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
class RolePermissionsRepository():
    db = Session(bind=engine, expire_on_commit=False)

    # Role
    def getListRole(self, limit: int = 10, skip: int = 0):
        return  self.db.query(Role).offset(skip).limit(limit).all()

    def createRole(self, roleData, response):
        checkRoleExists = self.db.query(Role).filter(Role.name == roleData.name).first()
        if checkRoleExists:
            response.status_code=status.HTTP_400_BAD_REQUEST
            response.body = {
                "status": False,
                "message": f"{roleData.name} already exists"
            }
            return response.body
        self.db.add(roleData)
        self.db.commit()
        self.db.refresh(roleData)
        response.status_code=status.HTTP_201_CREATED
        response.body = {
                    "status": True,
                    "message": "Role created successfully"
                }
        return response.body

    # Permission
    def getListPermission(self, limit: int = 10, skip: int = 0):
        return  self.db.query(Permission).offset(skip).limit(limit).all()

    def createPermission(self, permissionData, response):
        checkPermissionExists = self.db.query(Permission).filter(Permission.name == permissionData.name).first()
        if checkPermissionExists:
            response.status_code=status.HTTP_400_BAD_REQUEST
            response.body = {
                "status": False,
                "message": f"{permissionData.name} already exists"
            }
            return response.body
        self.db.add(permissionData)
        self.db.commit()
        self.db.refresh(permissionData)
        response.status_code=status.HTTP_201_CREATED
        response.body = {
                    "status": True,
                    "message": "Permission created successfully",
                }
        return response.body

    def createRolePermission(self, rolePermissionsData, response):
        self.db.query(Role).where(Role.id == rolePermissionsData.role_id).one()
        for permissionId in rolePermissionsData.permissions:
            checkRolePermissionExists = self.db.query(RolePermissions).where(RolePermissions.role_id == rolePermissionsData.role_id).where(RolePermissions.permission_id == permissionId).first()
            self.db.query(Permission).where(Permission.id == permissionId).one()
            if not checkRolePermissionExists:
                permission = RolePermissions(role_id=rolePermissionsData.role_id, permission_id=permissionId)
                self.db.add(permission)
                self.db.commit()
                self.db.refresh(permission)

        response.status_code=status.HTTP_201_CREATED
        response.body = {
                    "status": True,
                    "message": "Role Permissions created successfully",
                }
        return response.body

    def assignUserRoles(self, userRolesData, response):
        self.db.query(Role).where(Role.id == userRolesData.role_id).one()
        self.db.query(User).where(User.id == userRolesData.user_id).one()
        checkUserRoleExists = self.db.query(UserRoles).where(UserRoles.role_id == userRolesData.role_id).where(UserRoles.user_id == userRolesData.user_id).first()
        if checkUserRoleExists:
            response.status_code=status.HTTP_400_BAD_REQUEST
            response.body = {
                        "status": False,
                        "message": "User Role already assigned",
                    }
            return response.body

        userRole = UserRoles(role_id=userRolesData.role_id, user_id=userRolesData.user_id)
        self.db.add(userRole)
        self.db.commit()
        self.db.refresh(userRole)

    def getRolesPermissions(self, role_id):
        return self.db.query(Role).filter(Role.id == role_id).options(
        joinedload(Role.permissions).joinedload(RolePermissions.permission)).first()

    def getUserRole(self, user_id):
        return self.db.query(User).filter(User.id == user_id).options(
        joinedload(User.roles).joinedload(UserRoles.role)).first()