import uuid
from sqlalchemy.orm import Session
from models.user import UserModel
from schemas.user import RegisterUser, UpdateUser


def create_user(db: Session, user_data: RegisterUser):
    user = UserModel(
        id=str(uuid.uuid4()),
        name=user_data.name,
        email=user_data.email,
        password=user_data.password  # you should hash it!
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: str):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_users(db: Session):
    return db.query(UserModel).all()


def update_user(db: Session, user_id: str, user_data: UpdateUser):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: str):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
