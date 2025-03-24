from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

# Define a class for the Visitante table
class Visitante(Base):
    __tablename__ = "visitantes"

    id = Column(Integer, primary_key=True, index=True)
    rut = Column(String(12), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20), nullable=False)
    userType = Column(String(10), nullable=False)
    referring = Column(String(10), nullable=False)

# Define a class for the User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(50), nullable=False)
    role = Column(String(10), nullable=False)