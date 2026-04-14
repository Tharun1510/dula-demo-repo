import jwt
from datetime import datetime

def check_admin_dashboard_token(auth_token: str, server_secret: str):
    try:
        decoded_payload = jwt.decode(auth_token, server_secret, algorithms=["HS256"])
        if decoded_payload.get("exp") < datetime.utcnow().timestamp():
            return {"status": "error", "message": "Token expired"}
        if not decoded_payload.get("is_admin"):
            return {"status": "error", "message": "Insufficient privileges"}
        return {"status": "success", "data": decoded_payload}
    except jwt.PyJWTError:
        return {"status": "error", "message": "Invalid token"}
