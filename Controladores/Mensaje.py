from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from Modelos.Mensaje import Mensaje
from Schemas.MensajeBase import MensajeOut, MensajeCreate
from Database import get_db
from typing import List


router = APIRouter()

@router.get("/mensajes", response_model=List[MensajeOut])
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Mensaje).all()


@router.get("/mensajes/{mensaje_id}", response_model=MensajeOut)
def get_transaction_by_id(mensaje_id: int, db: Session = Depends(get_db)):
    tx = db.query(Mensaje).filter(Mensaje.id == mensaje_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@router.post("/mensajes/", response_model=MensajeOut)
def create_user(user: MensajeCreate):
    return {
        "id": 1,
        "currency": user.name,
    }
