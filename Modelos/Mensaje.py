from sqlalchemy import Column, Integer, String, Text
from Database.Database import Base

class Mensaje(Base):
    __tablename__ = "mensajes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    mensaje = Column(Text)
    comando = Column(String)
    amount = Column(String)
    timestamp = Column(String)

    def __init__(self, user_id, mensaje, comando, amount):
        self.user_id = user_id
        self.mensaje = mensaje
        self.comando = comando
        self.amount = amount
