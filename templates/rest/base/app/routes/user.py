from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from app.data.database import get_db
from app.schemas.user import RegisterUser, LoginUser, User, UpdateUser
from app.controllers import user as user_controller
from app.utils.rate_limiter import get_rate_limiter
from app.dependencies.auth import auth_user_id

router = APIRouter(prefix="/users", tags=["Users"])

login_limiter = get_rate_limiter(5, 60)
register_limiter = get_rate_limiter(3, 60)
private_limiter = get_rate_limiter(10, 60)


@router.post("/register", response_model=User, dependencies=[Depends(register_limiter)])
def register(user: RegisterUser, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)


@router.post("/login", response_model=User, dependencies=[Depends(login_limiter)])
def login(user: LoginUser, db: Session = Depends(get_db)):
    return user_controller.login_user(db, user)


@router.get("/me", response_model=User, dependencies=[Depends(private_limiter)])
def get_me(user_id: str = Depends(auth_user_id), db: Session = Depends(get_db)):
    return user_controller.get_user_by_id(db, user_id)


@router.put("/me", response_model=User, dependencies=[Depends(private_limiter)])
def update_me(update: UpdateUser, user_id: str = Depends(auth_user_id), db: Session = Depends(get_db)):
    return user_controller.update_user(db, user_id, update)


@router.delete("/me", dependencies=[Depends(private_limiter)])
def delete_me(user_id: str = Depends(auth_user_id), db: Session = Depends(get_db)):
    deleted = user_controller.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
