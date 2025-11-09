# Wallet API

This project is a backend API built with **FastAPI** and **SQLite** that manages users, wallets, and payment transactions. It also stores incoming WhatsApp-style messages, linking them to users in the system based on their phone numbers.

## Features

- User registration and retrieval
- Wallet creation and balance management
- Transaction creation between wallets
- Message logging associated with each user via phone lookup
- Fully RESTful API powered by FastAPI
- SQLite database with SQLAlchemy ORM

## Project Structure
```

│
├─ main.py
├─ Database.py
│
├─ Modelos/
│   ├─ Usuario.py
│   ├─ Wallet.py
│   └─ Mensaje.py
│   └─ Transaction.py
│
├─ Schemas/
│   ├─ UserBase.py
│   ├─ WalletBase.py
│   ├─ MensajeBase.py
│   └─ TransactionBase.py
│
└─ Controladores/
    ├─ Usuario.py
    ├─ Wallet.py
    ├─ Mensaje.py
    └─ Transaction.py
```

---

## Requirements

- Python 3.9+
- pip (Python package manager)

---

## Installation

- 1 **Clone the repository**

```
git clone <your-repo-url>
cd project
```
Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

Running the Application
Start the FastAPI development server:
```
uvicorn main:app --reload
```
The API will be available at:
```
http://127.0.0.1:8000
```
Interactive API Docs (Swagger UI):
```
http://127.0.0.1:8000/docs
```

## API Highlights

| Resource     | Method | Endpoint            | Description                            |
| ------------ | ------ | ------------------- | -------------------------------------- |
| Users        | `POST` | `/api/users`        | Create a new user                      |
| Users        | `GET`  | `/api/users`        | List all users                         |
| Wallets      | `POST` | `/api/wallets`      | Create a wallet                        |
| Transactions | `POST` | `/api/transactions` | Create a transaction                   |
| Messages     | `POST` | `/api/mensajes`     | Store a message linked by phone number |

Example JSON Request Bodies

Create User
```
{
  "name": "Alice",
  "phone": "+5215512345678",
  "interledger_wallet_id": "abc123",
  "wa_user_id": "wa_001",
  "clabe": "123456789012345678",
  "verified": true,
  "password": "secret123"
}
```
Create Wallet
```
{
  "interledger_wallet_id": "wallet_user_1",
  "user_id": 1,
  "balance": 0.0,
  "currency": "MXN"
}
```
Create Transaction
```
{
  "payer_wallet_id": 1,
  "payee_wallet_id": 2,
  "amount": 150,
  "currency": "MXN",
  "status": "pending"
}
```
Create Message
```
{
  "phone_number": "+5215512345678",
  "mensaje": "Send payment",
  "comando": "SEND",
  "amount": "150"
}
```

## Notes
You can switch to PostgreSQL or MySQL by changing the database URL inside Database.py.
To enable authentication or JWT token support, session middleware can be added later.

## License
This project is provided without warranty, for educational and product development use.
