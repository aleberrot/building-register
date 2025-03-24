from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from sqlalchemy.orm import Session
from models import User
from database import get_db

# Initializes the router
# prefix: /auth
# tags: Authentication
router = APIRouter(prefix="/auth", tags=["Authenticacion"])

# Schema for the user
class UserSchemaCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

    def model_dump(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }

# Schema for the user response
class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    class config:
        orm_mode = True

# TODO register route
@router.post("/register")
async def register(user: UserSchemaResponse, db: Session = Depends(get_db)):
    # Create a new user object
    new_user = User(**user.model_dump())
    try:
        # Add the new user to the database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    except:
        # If the user is already registered, rollback the transaction
        db.rollback()
        raise HTTPException(status_code=400, detail="Usuario ya registrado")

# TODO login route
@router.post("/login")
async def login(user: UserSchemaResponse, db: Session = Depends(get_db)):
    # Query the database for the user
    user_db = db.query(User).filter(User.username == user.username).first()
    # If the user exists and the password is correct, return the user
    if user_db and user_db.password == user.password:
        return user_db
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# TODO pending hashing password function

# TODO pending token generation function

# TODO pending token validation function

# TODO pending password validation function