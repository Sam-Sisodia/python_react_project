
from sqlalchemy import Column, Integer, String, Boolean,Enum
# from app.models.base import Base
from  db.session import Base


from enum  import Enum as Pynum


class UserRole(Pynum):
    INDIVIDUAL = "individual"
    ENTERPRISE = "enterprise"
    GOVERNMENT = "government"



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # user_type = Column(Enum(UserRole), default=UserRole.value)
    user_type = Column(Enum(UserRole), default=None, nullable=True)
 