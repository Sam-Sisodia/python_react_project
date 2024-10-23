from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr  # Add type annotations
    password: str
    user_type: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
