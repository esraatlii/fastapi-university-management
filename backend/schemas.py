from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, EmailStr

class UserRole(str,Enum):
    admin = "admin"
    dean = "dean"
    department_rep = "department_rep"

class UserCreate(BaseModel):
    """
    Frontend'ten /api/register isteği ile gelecek body
    """
    full_name : str = Field(..., min_length=1, max_length=100)
    email : EmailStr
    password : str
    role: UserRole
    department_id: Optional[int] = None

class UserOut(BaseModel):
    """
    Backend'ten frontend' e dönecek response
    """
    full_name : str = Field(..., min_length=1, max_length=100)
    email : EmailStr
    role: UserRole
    department_id: Optional[int] = None

    class Config:
        orm_mode = True


class Login(BaseModel):
    email : EmailStr
    password : str