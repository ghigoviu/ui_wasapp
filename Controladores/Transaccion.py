from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Modelos.Transaction import Transaction
from Schemas.TransactionBase import TransactionOut
from Database import get_db
from typing import List

router = APIRouter()

@router.get("/transactions", response_model=List[TransactionOut])
def get_all_transactions(db: Session = Depends(get_db)):
    """Return all transactions from DB"""
    return db.query(Transaction).all()


@router.get("/transactions/{transaction_id}", response_model=TransactionOut)
def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    """Return a transaction by ID"""
    tx = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx
