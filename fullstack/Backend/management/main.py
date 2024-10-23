# app/main.py
from fastapi import FastAPI
# from app.api.v1.endpoints.user import router as user_router
from db.session import engine,Base
from app.api.v1.endpoints import user


# from app.models import user  # Import your models so Base can recognize them
# from app.db.base import Base  # Import Base

# # Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])

app.include_router(user.router, prefix="/api/v1", tags=["users"])