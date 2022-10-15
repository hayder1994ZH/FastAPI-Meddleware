from config.moduls import Role, Permission
from Repositories.RolePermissionsRepository import RolePermissionsRepository

class RolePermissionController:
    def __init__(self, RolePermissionRepo = RolePermissionsRepository()):
        self.RolePermissionRepo = RolePermissionRepo

    def getListRole(self, take, skip):
        return self.RolePermissionRepo.getListRole()
        
    def createRole(self, request, response):
        role = Role(name=request.name)
        return self.RolePermissionRepo.createRole(role, response)

    def getPermission(self, take, skip):
        return self.RolePermissionRepo.getListPermission()
        
    def createPermission(self, request, response):
        permission = Permission(name=request.name)
        return self.RolePermissionRepo.createPermission(permission, response)
        
    def createRolePermission(self, request, response):
        return self.RolePermissionRepo.createRolePermission(request, response)
        
    def assignUserRoles(self, request, response):
        return self.RolePermissionRepo.assignUserRoles(request, response)
    
    def getRolePermission(self, id):
        return self.RolePermissionRepo.getRolesPermissions(id)

    def getUserRole(self, id):
        return self.RolePermissionRepo.getUserRole(id)