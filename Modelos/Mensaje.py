from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from Database.Database import Base

class Mensaje(Base):
    __tablename__ = "mensajes"

    id = Column(Integer, primary_key=True, index=True)
    to = Column(String, nullable=True)
    mensaje = Column(Text)
    comando = Column(String)
    amount = Column(String)
    timestamp = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="mensajes")

    def __init__(self, user_id, mensaje, comando, amount, timestamp):
        self.user_id = user_id
        self.mensaje = mensaje
        self.comando = comando
        self.amount = amount
        self.timestamp = timestamp
