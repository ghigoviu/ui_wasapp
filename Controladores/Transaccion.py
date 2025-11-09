from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Modelos.Transaction import Transaction
from Modelos.Wallet import Wallet
from Schemas.TransactionBase import TransactionOut, TransactionCreate
from Database import get_db
from typing import List

router = APIRouter()

@router.get("/transactions", response_model=List[TransactionOut])
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


@router.get("/transactions/{transaction_id}", response_model=TransactionOut)
def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    tx = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@router.post("/transactions", response_model=TransactionOut)
def create_transaction(tx: TransactionCreate, db: Session = Depends(get_db)):

    payer = db.query(Wallet).filter(Wallet.id == tx.payer_wallet_id).first()
    payee = db.query(Wallet).filter(Wallet.id == tx.payee_wallet_id).first()

    if not payer:
        raise HTTPException(status_code=404, detail="Payer wallet not found")

    if not payee:
        raise HTTPException(status_code=404, detail="Payee wallet not found")

    if payer.id == payee.id:
        raise HTTPException(status_code=400, detail="Cannot send a transaction to the same wallet")

    if payer.balance < tx.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Crear transacción
    new_tx = Transaction(
        payer_wallet_id=tx.payer_wallet_id,
        payee_wallet_id=tx.payee_wallet_id,
        amount=tx.amount,
        currency=tx.currency,
        concept=tx.concept,
        status="success",
        preferred_method=tx.preferred_method
    )

    payer.balance -= tx.amount
    payee.balance += tx.amount

    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)

    return new_tx