from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class MensajeBase(BaseModel):
    user_id: int
    mensaje: str
    comando: str
    amount: str


class MensajeCreate(MensajeBase):
    pass


class MensajeOut(MensajeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
