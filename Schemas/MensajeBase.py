from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class MensajeBase(BaseModel):
    user_id: int
    mensaje: str
    comando: str
    amount: str


class MensajeCreate(BaseModel):
    phone_number: str
    mensaje: str
    comando: str
    amount: str


class MensajeOut(MensajeBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
