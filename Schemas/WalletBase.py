from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class WalletBase(BaseModel):
    interledger_wallet_id: str
    user_id: int
    balance: float = 0.0
    clabe: Optional[str] = None
    pin_hash: Optional[str] = None
    state_context: Optional[str] = None
    currency: str = "MXN"
    account_address: Optional[str] = None


class WalletCreate(WalletBase):
    pass


class WalletUpdate(BaseModel):
    balance: Optional[float] = None
    state_context: Optional[str] = None


class WalletOut(WalletBase):
    id: int
    registration_timestamp: datetime

    class Config:
        orm_mode = True