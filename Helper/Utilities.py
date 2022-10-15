from fastapi import FastAPI, Depends, Response, status, HTTPException
from Models.Authintecation.Oauth2 import get_current_user
from Models.User import User

class Utilities:
    @staticmethod
    def get_acive_user(current_user: User = Depends(get_current_user)):
        if not current_user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return current_user
        
