

from sqlalchemy.orm import Session

from  db.session import get_db
from models.user import User


from schema.schemas import UserCreate ,UserResponse

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        hashed_password=user.password,
        user_type=user.user_type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user