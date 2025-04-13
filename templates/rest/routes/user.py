from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database import SessionLocal
from schemas.user import RegisterUser, User, UpdateUser
from controllers import user as user_controller

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=User)
def create_user(user: RegisterUser, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)


@router.get("/", response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = user_controller.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: UpdateUser, db: Session = Depends(get_db)):
    updated = user_controller.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleted = user_controller.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
