from sqlalchemy import Column, Integer, String, Float
from Database.Database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    interledger_wallet_id = Column(String, index=True)
    user_id = Column(String, index=True)
    balance = Column(Float)
    pin_hash = Column(String)
    currency = Column(String,default="MXN")
    state_context = Column(String)
    account_address = Column(String)
