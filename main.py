# from fastapi import FastAPI
# from routers.user_router import router as user_router

# app = FastAPI()

# app.include_router(user_router, prefix="/api")

from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.user_router import router as user_router

app = FastAPI()

# Include routers
app.include_router(auth_router, prefix="/api/auth")
app.include_router(user_router, prefix="/api/user")