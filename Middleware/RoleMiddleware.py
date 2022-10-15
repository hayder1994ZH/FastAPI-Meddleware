from fastapi import FastAPI, HTTPException, Depends
from config.moduls import User
from Models.Authintecation.Oauth2 import get_current_active_user, get_current_user

class RoleMiddleware:
    @staticmethod
    def permissions(permission, userAuthInfo):
        for i in userAuthInfo:
            if i == permission:
                return True
        raise HTTPException(status_code=403, detail="Permission denied")
        