from typing import List

from fastapi import APIRouter, HTTPException
from Schemas.UserBase import UserOut
from Schemas.WalletBase import WalletOut
from Schemas.TransactionBase import TransactionOut

router = APIRouter()

@router.get("/users", response_model=List[UserOut])
def get_all_users():
    """Return all users"""
    return fake_users


@router.get("/users/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int):
    """Return a user by ID"""
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# =========================================================
# 💳 WALLET CONTROLLERS
# =========================================================

@router.get("/wallets", response_model=List[WalletOut])
def get_all_wallets():
    """Return all wallets"""
    return fake_wallets


@router.get("/wallets/{wallet_id}", response_model=WalletOut)
def get_wallet_by_id(wallet_id: int):
    """Return a wallet by ID"""
    wallet = next((w for w in fake_wallets if w["id"] == wallet_id), None)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet


# =========================================================
# 💸 TRANSACTION CONTROLLERS
# =========================================================

@router.get("/transactions", response_model=List[TransactionOut])
def get_all_transactions():
    """Return all transactions"""
    return fake_transactions


@router.get("/transactions/{transaction_id}", response_model=TransactionOut)
def get_transaction_by_id(transaction_id: int):
    """Return a transaction by ID"""
    tx = next((t for t in fake_transactions if t["id"] == transaction_id), None)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx