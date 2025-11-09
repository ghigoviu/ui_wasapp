from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from Modelos.Usuario import Usuario
from Modelos.Wallet import Wallet
from Schemas.WalletBase import WalletOut, WalletCreate
from Database import get_db
from typing import List


router = APIRouter()

@router.get("/wallets", response_model=List[WalletOut])
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Wallet).all()


@router.get("/wallets/{wallet_id}", response_model=WalletOut)
def get_transaction_by_id(wallet_id: int, db: Session = Depends(get_db)):
    tx = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.post("/wallets", response_model=WalletOut)
def create_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):

    # Verificar que el usuario exista
    user = db.query(Usuario).filter(Usuario.id == wallet.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # (Opcional) Verificar que no existan dos wallets con mismo interledger ID
    existing_wallet = db.query(Wallet).filter(
        Wallet.interledger_wallet_id == wallet.interledger_wallet_id
    ).first()

    if existing_wallet:
        raise HTTPException(status_code=400, detail="Wallet already registered")

    # Crear la wallet
    new_wallet = Wallet(
        interledger_wallet_id=wallet.interledger_wallet_id,
        user_id=wallet.user_id,
        balance=wallet.balance,
        clabe=wallet.clabe,
        state_context=wallet.state_context,
        currency=wallet.currency,
        account_address=wallet.account_address
    )

    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)

    return new_wallet
