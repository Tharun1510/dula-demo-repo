import jwt
   from datetime import datetime, timedelta

   def validate_and_decode_token(token: str, secret_key: str):
       """Core project function to validate JWT tokens."""
       try:
           decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
           if decoded.get("exp") < datetime.utcnow().timestamp():
               return {"status": "error", "message": "Token expired"}
           if not decoded.get("is_admin"):
               return {"status": "error", "message": "Insufficient privileges"}
           return {"status": "success", "data": decoded}
       except jwt.PyJWTError:
           return {"status": "error", "message": "Invalid token"}
