from dotenv import load_dotenv
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from twilio.rest import Client
from pydantic import BaseModel

from Database import get_db
from UseCases import account_sid, auth_token, twilio_whatsapp_number
from test.models.Message import Message

load_dotenv()
router = APIRouter()
client = Client(account_sid, auth_token)

class MessageRequest(BaseModel):
    to: str
    message: str

@router.post("/send_message")
async def send_message(request: MessageRequest, db: Session = Depends(get_db)):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=request.message,
            to=f"whatsapp:{request.to}"
        )
        # Guardar en BD
        db_message = Message(
            sid=message.sid,
            to=request.to,
            message=request.message,
            status="success",
            command="none",
            amount=0
        )
        db.add(db_message)
        db.commit()
        db.refresh(db_message)

        return {
            "status": "success",
            "sid": message.sid,
            "to": request.to,
            "message": request.message,
            "command": db_message.command,
            "amount": db_message.amount
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
