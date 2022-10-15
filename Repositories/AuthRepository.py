from Repositories.BaseRepository import BaseRepository
from fastapi import HTTPException, status
from Models.Authintecation.Hash import verify_password
from Models.Authintecation.JWTtoken import create_access_token
class AuthRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)

    def login(self, request, response):
        user = self.db.query(self.model).filter_by(username = request.username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        if not verify_password(request.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong password')
        
        access_token = create_access_token(data={"sub": user.username})
        response.status_code=status.HTTP_200_OK
        response.body = {
                    "access_token": access_token,
                    "token_type": "bearer",
                    "status": True,
                    "message": "login successfully",
                    'data': user
                }
        return response.body
    
    