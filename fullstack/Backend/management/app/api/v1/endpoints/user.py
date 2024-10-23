


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.schemas import UserCreate ,UserResponse
from  db.session import get_db
from models.user import User
from services.utils import create_user
router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)