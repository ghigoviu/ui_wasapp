from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

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

