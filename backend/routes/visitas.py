from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from models import Visitante
from sqlalchemy.orm import Session
from database import get_db
from typing import List


# Initializes the router
# prefix: /visitas
# tags: Visitas

router = APIRouter(prefix="/visitas", tags=["Visitas"])

# List to store visitors
#visitors_db: List[dict] = []


# Schema for the visitor
class VisitanteSchema(BaseModel):
    name: str
    age: int
    rut: str
    email: str
    phone: str
    last_name: str
    referring: str
    userType: str

# Route to add a new visitor
# POST /visitas
# Request Body: Visitante
# Don't add name to route, the prefix is already defined in the router
@router.post("/")
async def add_visitor(visitor: VisitanteSchema, db: Session = Depends(get_db)):
    new_visitor = Visitante(**visitor.dict())
    db.add(new_visitor)
    db.commit()
    db.refresh(new_visitor)
    return new_visitor

# Route to get all visitors
# GET /visitas
# Don't add name to route, the prefix is already defined in the router
@router.get("/", response_model=List[VisitanteSchema])
async def get_visitors(db: Session = Depends(get_db)):
    return db.query(Visitante).all()

# Route to get a visitor by rut
# GET /visitas/{rut}
# @router.get("/{rut}")
# async def get_visitor(rut: str):
#     for visitor in visitors_db:
#         if visitor["rut"] == rut:
#             return {"data": visitor}
#     return {"mensaje": "Visitante no encontrado"}

# # Route to delete a visitor by rut
# # DELETE /visitas/{rut}
# @router.delete("/{rut}")
# async def delete_visitor(rut: str):
#     for visitor in visitors_db:
#         if visitor["rut"] == rut:
#             visitors_db.remove(visitor)
#             return {"mensaje": "Visitante eliminado exitosamente"}
#     return {"mensaje": "Visitante no encontrado"}

# # Route to update a visitor by rut
# # PUT /visitas/{rut}
# @router.put("/{rut}")
# async def update_visitor(rut: str, visitor: Visitante):
#     for visitor in visitors_db:
#         if visitor["rut"] == rut:
#             visitor["name"] = visitor.name
#             visitor["age"] = visitor.age
#             visitor["email"] = visitor.email
#             visitor["phone"] = visitor.phone
#             visitor["last_name"] = visitor.last_name
#             visitor["userType"] = visitor.userType
#             visitor["referring"] = visitor.referring
#             return {"mensaje": "Visitante actualizado exitosamente"}
#     return {"mensaje": "Visitante no encontrado"}