from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import Request

from database import SessionLocal
from models.Message import Message
from database import Base, engine
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from twilio.rest import Client
import os
from pydantic import BaseModel


class MessageRequest(BaseModel):
    to: str
    message: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

# Cargar variables de entorno
load_dotenv()

# Inicializar FastAPI
app = FastAPI(title="WhatsApp API via Twilio")

# Inicializar cliente Twilio
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(account_sid, auth_token)

@app.post("/send_message")
async def send_message(request: MessageRequest, db: Session = Depends(get_db)):
    try:
        message = client.messages.create(
            from_=twilio_whatsapp_number,
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

@app.post("/webhook")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    form = await request.form()

    from_number = form.get("From", "").replace("whatsapp:", "")
    incoming_message = form.get("Body", "")

    # Guardamos en la base de datos
    db_message = Message(
        sid=None,
        to=from_number,
        message=incoming_message,
        status="received",
        command="none",
        amount=0
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    print(f"📥 Mensaje recibido de {from_number}: {incoming_message}")

    return "OK"

