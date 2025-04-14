import uuid
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.utils.email import send_email

RESET_TOKEN_EXPIRY_MINUTES = 15

# In-memory storage for demo, use DB/Redis for prod
reset_tokens = {}


def generate_reset_token(user: UserModel) -> str:
    token = str(uuid.uuid4())
    expiry = datetime.now() + timedelta(minutes=RESET_TOKEN_EXPIRY_MINUTES)
    reset_tokens[token] = {"email": user.email, "expires": expiry}
    return token


def verify_reset_token(token: str):
    data = reset_tokens.get(token)
    if not data or data["expires"] < datetime.now():
        return None
    return data["email"]
