from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from Modelos.Usuario import Usuario
from Schemas.UserBase import UserOut, UserCreate
from Database import get_db
from typing import List


router = APIRouter()

@router.get("/users", response_model=List[UserOut])
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@router.get("/users/{user_id}", response_model=UserOut)
def get_transaction_by_id(usuario_id: int, db: Session = Depends(get_db)):
    tx = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(Usuario).filter(Usuario.phone == user.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    new_user = Usuario(
        name=user.name,
        phone=user.phone,
        interledger_wallet_id=user.interledger_wallet_id,
        wa_user_id=user.wa_user_id,
        verified=user.verified,
        pin=user.pin
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user