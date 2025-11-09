from sqlalchemy import Column, Integer, String, Boolean
from Database.Database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    interledger_wallet_id = Column(String)
    wa_user_id = Column(String)
    verified = Column(Boolean)
    pin = Column(String)
