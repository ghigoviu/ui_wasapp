from sqlalchemy import Column, Integer, String, Float
from Database.Database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    type = Column(String)  # 'income', 'expense', etc.
