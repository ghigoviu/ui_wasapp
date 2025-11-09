from controllers import router
from fastapi import FastAPI
from Schemas.UserBase import UserCreate, UserOut

app = FastAPI()

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate):
    # Aquí guardarías el usuario en la base de datos
    return {
        "id": 1,
        "name": user.name,
        "phone": user.phone,
        "registration_timestamp": "2025-11-08T20:00:00Z"
    }

app = FastAPI(title="Wallet API")

app.include_router(router, prefix="/api", tags=["API"])

# Para probar:
# http://127.0.0.1:8000/api/users
# http://127.0.0.1:8000/api/wallets
# http://127.0.0.1:8000/api/transactions

# Cómo ejecutar
# uvicorn main:app --reload
