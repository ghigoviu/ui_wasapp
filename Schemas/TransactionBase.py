from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
    payer_wallet_id: int
    payee_wallet_id: int
    amount: float
    currency: str
    concept: str
    preferred_method: str

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    status: str = "pending"

    class Config:
        from_attributes = True
