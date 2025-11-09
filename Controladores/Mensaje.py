from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from datetime import datetime

from Modelos.Mensaje import Mensaje
from Modelos.Usuario import Usuario
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


@router.post("/mensajes", response_model=MensajeOut)
def crear_mensaje(data: MensajeCreate, db: Session = Depends(get_db)):
    # 1. Buscar usuario por número telefónico
    usuario = db.query(Usuario).filter(Usuario.phone == data.phone_number).first()
    current_timestamp = datetime.now().isoformat()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado con ese número.")

    # 2. Crear el mensaje
    nuevo_mensaje = Mensaje(
        mensaje=data.mensaje,
        comando=data.comando,
        amount=data.amount,
        user_id=usuario.id,
        timestamp=current_timestamp
    )

    db.add(nuevo_mensaje)
    db.commit()
    db.refresh(nuevo_mensaje)

    return nuevo_mensaje
