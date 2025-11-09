from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

# =========================================================
# 💸 TRANSACTION SCHEMAS
# =========================================================

class TransactionBase(BaseModel):
    payer_wallet_id: int
    payee_wallet_id: int
    amount: float
    currency: str = "MXN"
    concept: Optional[str] = None
    status: str = "pending"
    preferred_method: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    status: Optional[str] = None


class TransactionOut(TransactionBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True