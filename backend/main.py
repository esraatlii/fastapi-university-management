from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = [
    "*",  # Geliştirme sürecinde her yerden erişime izin ver
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # OPTIONS dahil tüm metodlara izin ver
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root():
    return {"Message": "Uygulama çalışıyor"}

@app.post("/api/register",response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: db_dependency):
    existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Bu e-posta ile zaten bir kullanıcı mevcut"
        )

    new_user = models.Users(
        full_name=user.full_name,
        email=user.email,
        password_hash = user.password,
        role = user.role,
        department_id = user.department_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/login",response_model=schemas.UserOut)
def login(login_data: schemas.Login, db: db_dependency):
    user = db.query(models.Users).filter(models.Users.email == login_data.email).first()
    if not user or user.password_hash != login_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="E-posta veya şifre hatalı"
                            )
    return user