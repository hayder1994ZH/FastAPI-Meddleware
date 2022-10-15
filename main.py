from fastapi import FastAPI, HTTPException
from routers import  user, login, post, rolePermission
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
app = FastAPI()



async def catch_exceptions_middleware(request: Request, call_next):
    try:
        print("request:", request.method)
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(status_code=500, content=jsonable_encoder({"message": exc.args[0]}))
        
app.middleware('http')(catch_exceptions_middleware)
app.include_router(login.router)
app.include_router(rolePermission.router)
app.include_router(user.router)
app.include_router(post.router)
@app.get("/", tags=["Root"])
def root():
    return  'welcome to my blog'