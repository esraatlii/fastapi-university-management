from sqlalchemy import  Column, Integer,String
from database import  Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String,index=True,nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String,nullable=False)
    role = Column(String,index=True,nullable=False)
    department_id = Column(Integer,index=True,nullable=True)
