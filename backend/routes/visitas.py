from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# Initializes the router
# prefix: /visitas
# tags: Visitas

router = APIRouter(prefix="/visitas", tags=["Visitas"])

visitors_db: List[dict] = []

class Visitante(BaseModel):
    name: str
    age: int
    rut: str
    email: str
    phone: str

# Route to add a new visitor
# POST /visitas
# Request Body: Visitante
# Don't add name to route, the prefix is already defined in the router
@router.post("/")
async def add_visitor(visitor: Visitante):
    print("request made")
    visitors_db.append({"rut": visitor.rut, "name": visitor.name, "age": visitor.age, "email": visitor.email, "phone": visitor.phone})
    return {"mensaje": "Visitante agregado exitosamente", "data":{"rut": visitor.rut, "name": visitor.name, "age": visitor.age, "email": visitor.email, "phone": visitor.phone}}

# Route to get all visitors
# GET /visitas
# Don't add name to route, the prefix is already defined in the router
@router.get("/")
async def get_visitors():
    return {"data": visitors_db}

# Route to get a visitor by rut
# GET /visitas/{rut}
@router.get("/{rut}")
async def get_visitor(rut: str):
    for visitor in visitors_db:
        if visitor["rut"] == rut:
            return {"data": visitor}
    return {"mensaje": "Visitante no encontrado"}

# Route to delete a visitor by rut
# DELETE /visitas/{rut}
@router.delete("/{rut}")
async def delete_visitor(rut: str):
    for visitor in visitors_db:
        if visitor["rut"] == rut:
            visitors_db.remove(visitor)
            return {"mensaje": "Visitante eliminado exitosamente"}
    return {"mensaje": "Visitante no encontrado"}
