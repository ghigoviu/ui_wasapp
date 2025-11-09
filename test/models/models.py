from sqlalchemy import Column, Integer, String
from test.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sid = Column(String, index=True)
    to = Column(String)
    message = Column(String)
    status = Column(String)
    command = Column(String, default="none")
    amount = Column(Integer, default=0)
