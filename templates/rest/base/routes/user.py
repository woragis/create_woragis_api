from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from data.database import SessionLocal
from schemas.user import RegisterUser, LoginUser, User, UpdateUser
from controllers import user as user_controller
from utils.rate_limiter import get_rate_limiter
from dependencies.auth import auth_user_id

router = APIRouter(prefix="/users", tags=["Users"])

login_limiter = get_rate_limiter(5, 60)
register_limiter = get_rate_limiter(3, 60)
private_limiter = get_rate_limiter(10, 60)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=User)
def register(user: RegisterUser, db: Session = Depends(get_db), request: Request = Depends(register_limiter)):
    return user_controller.create_user(db, user)


@router.post("/login", response_model=User)
def login(user: LoginUser, db: Session = Depends(get_db), request: Request = Depends(login_limiter)):
    return user_controller.login_user(db, user)


@router.get("/me", response_model=User)
def get_me(user_id: str = Depends(auth_user_id), db: Session = Depends(get_db), request: Request = Depends(private_limiter)):
    return user_controller.get_user_by_id(db, user_id)


@router.put("/me", response_model=User)
def update_me(update: UpdateUser, user_id: str = Depends(auth_user_id), db: Session = Depends(get_db), request: Request = Depends(private_limiter)):
    return user_controller.update_user(db, user_id, update)


@router.delete("/me")
def delete_me(user_id: str = Depends(auth_user_id), db: Session = Depends(get_db), request: Request = Depends(private_limiter)):
    deleted = user_controller.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
