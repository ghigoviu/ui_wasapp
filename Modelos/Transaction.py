from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from Database.Database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    payer_wallet_id = Column(Integer, ForeignKey("wallets.id"))
    payee_wallet_id = Column(Integer, ForeignKey("wallets.id"))
    amount = Column(Float, nullable=False)
    currency = Column(String, default="MXN")
    concept = Column(String, nullable=True)
    status = Column(String, default="pending")
    preferred_method = Column(String, nullable=True)

    payer_wallet = relationship("Wallet", foreign_keys=[payer_wallet_id])
    payee_wallet = relationship("Wallet", foreign_keys=[payee_wallet_id])