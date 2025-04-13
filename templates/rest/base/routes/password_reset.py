from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from data.database import get_db
from models.user import UserModel
from controllers.password_reset import generate_reset_token, verify_reset_token
from utils.email import send_email
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/forgot-password")
def forgot_password(request: Request, email: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    token = generate_reset_token(user)
    reset_link = f"{request.base_url}auth/reset-password?token={token}"
    send_email("Password Reset", user.email, f"Click here: {reset_link}")
    return {"message": "Password reset email sent"}


@router.post("/reset-password")
def reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    email = verify_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password = bcrypt.hash(new_password)
    db.commit()
    return {"message": "Password reset successful"}
