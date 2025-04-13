from fastapi import HTTPException, Request
from jose import JWTError, jwt
from config.index import settings


def auth_user_id(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    try:
        payload = jwt.decode(
            token[7:], settings.JWT_SECRET, algorithms=["HS256"])
        return payload.get("sub")  # Return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
