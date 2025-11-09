from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    phone: str
    interledger_wallet_id: Optional[str] = None
    wa_user_id: Optional[str] = None
    verified: bool = False


class UserCreate(UserBase):
    pin: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    verified: Optional[bool] = None


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
