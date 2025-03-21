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
@router.get("/{rut}", response_model=VisitanteSchema)
async def get_visitor(rut: str, db: Session = Depends(get_db)):
    visitor  = db.query(Visitante).filter(Visitante.rut == rut).first()
    if visitor:
        return visitor
    raise HTTPException(status_code=404, detail="Visitante no encontrado")

# # Route to delete a visitor by rut
# # DELETE /visitas/{rut}
@router.delete("/{rut}", status_code=204)
async def delete_visitor(rut: str, db: Session = Depends(get_db)):
    visitor = db.query(Visitante).filter(Visitante.rut == rut).first()
    if visitor:
        db.delete(visitor)
        db.commit()
        return {"mensaje": "Visitante eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Visitante no encontrado")

# # Route to update a visitor by rut
# # PUT /visitas/{rut}
@router.put("/{rut}")
async def update_visitor(rut: str, visitor: VisitanteSchema, db: Session = Depends(get_db)):
    visitor_db = db.query(Visitante).filter(Visitante.rut == rut).first()
    if visitor_db:
        visitor_db.name = visitor.name
        visitor_db.age = visitor.age
        visitor_db.email = visitor.email
        visitor_db.phone = visitor.phone
        visitor_db.last_name = visitor.last_name
        visitor_db.userType = visitor.userType
        visitor_db.referring = visitor.referring
        db.commit()
        db.refresh(visitor_db)
        return visitor_db
    raise HTTPException(status_code=404, detail="Visitante no encontrado")