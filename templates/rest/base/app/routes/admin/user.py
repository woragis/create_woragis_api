from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.data.database import SessionLocal
from app.schemas.user import User, UpdateUser
from app.controllers import user as user_controller
from app.utils.rate_limiter import get_rate_limiter

router = APIRouter(prefix="/admin/users", tags=["Admin Users"])

admin_limiter = get_rate_limiter(20, 60)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[User])
def list_users(db: Session = Depends(get_db), request: Request = Depends(admin_limiter)):
    return user_controller.get_users(db)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: str, db: Session = Depends(get_db), request: Request = Depends(admin_limiter)):
    user = user_controller.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, update: UpdateUser, db: Session = Depends(get_db), request: Request = Depends(admin_limiter)):
    updated = user_controller.update_user(db, user_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db), request: Request = Depends(admin_limiter)):
    deleted = user_controller.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
