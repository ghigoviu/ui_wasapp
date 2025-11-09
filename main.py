from fastapi import FastAPI
from Controladores.Transaccion import router as transactions_router
from Controladores.Usuario import router as usuarios_router
from Controladores.Wallet import router as wallets_router
from Controladores.Mensaje import router as mensajes_router
from UseCases.SendMessage import router as send_message_router
from UseCases.ReceiveMessage import router as receive_message_router
from Database.Database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Wallet API")

app.include_router(transactions_router, prefix="/api", tags=["Transactions"])
app.include_router(usuarios_router, prefix="/api", tags=["Usuarios"])
app.include_router(wallets_router, prefix="/api", tags=["Wallets"])
app.include_router(mensajes_router, prefix="/api", tags=["Mensajes"])
app.include_router(send_message_router, prefix="/api", tags=["SendMessages"])
app.include_router(receive_message_router, prefix="/api", tags=["ReceiveMessages"])
