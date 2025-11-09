from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi import Request
from dotenv import load_dotenv

from Database import get_db
from test.models.Message import Message

load_dotenv()

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    form = await request.form()

    from_number = form.get("From", "").replace("whatsapp:", "")
    incoming_message = form.get("Body", "")

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
