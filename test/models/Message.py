from sqlalchemy import Column, Integer, String
from test.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sid = Column(String, index=True, nullable=True)
    to = Column(String)
    message = Column(String)
    status = Column(String)
    command = Column(String, default="none")
    amount = Column(Integer, default=0)

    def __init__(self, sid, to, message, status, command, amount):
        self.sid = sid
        self.to = to
        self.message = message
        self.status = status
        self.command = command
        self.amount = amount