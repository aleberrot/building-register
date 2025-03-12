from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/visitas", tags=["Visitas"])

visitors_db: List[dict] = []

class Visitante(BaseModel):
    name: str
    age: int
    rut: str
    email: str
    phone: str

@router.post("/visitas")
async def add_visitor(visitor: Visitante):
    print("request made")
    visitors_db.append({"rut": visitor.rut, "name": visitor.name, "age": visitor.age, "email": visitor.email, "phone": visitor.phone})
    return {"mensaje": "Visitante agregado exitosamente", "data":{"rut": visitor.rut, "name": visitor.name, "age": visitor.age, "email": visitor.email, "phone": visitor.phone}}

@router.get("/visitas")
async def get_visitors():
    return {"data": visitors_db}