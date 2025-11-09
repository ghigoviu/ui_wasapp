# --- Datos simulados (en un entorno real, esto se conecta a la DB) ---
fake_users = [
    {"id": 1, "name": "Alice", "phone": "5551234567", "interledger_wallet_id": "WALLET001", 
     "wa_user_id": "WA001", "tx_id": "TX001", "clabe": "123456789012345678", "verified": True, 
     "password": "hashed_pass", "registration_timestamp": datetime.utcnow()},
    {"id": 2, "name": "Bob", "phone": "5559876543", "interledger_wallet_id": "WALLET002", 
     "wa_user_id": "WA002", "tx_id": "TX002", "clabe": "987654321098765432", "verified": False, 
     "password": "hashed_pass2", "registration_timestamp": datetime.utcnow()}
]

fake_wallets = [
    {"interledger_wallet_id": "WALLET001", "id": 1, "user_id": 1, "balance": 5000.00, "clabe": "123456", 
     "pin_hash": "hash123", "state_context": "active", "currency": "MXN", "account_address": "ADDR001", 
     "registration_timestamp": datetime.utcnow()},
    {"interledger_wallet_id": "WALLET002", "id": 2, "user_id": 2, "balance": 200.50, "clabe": "654321", 
     "pin_hash": "hash321", "state_context": "frozen", "currency": "MXN", "account_address": "ADDR002", 
     "registration_timestamp": datetime.utcnow()}
]

fake_transactions = [
    {"id": 1, "payer_wallet_id": 1, "payee_wallet_id": 2, "amount": 100.0, "currency": "MXN", 
     "concept": "Payment", "timestamp": datetime.utcnow(), "status": "completed", 
     "preferred_method": "interledger"},
    {"id": 2, "payer_wallet_id": 2, "payee_wallet_id": 1, "amount": 50.0, "currency": "MXN", 
     "concept": "Refund", "timestamp": datetime.utcnow(), "status": "pending", 
     "preferred_method": "interledger"}
]
