import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from schemas.user import RegisterUser, UpdateUser, LoginUser

from utils.encryption import hash_password, verify_password
from utils.jwt import create_access_token


def create_user(db: Session, user_data: RegisterUser):
    hashed_password = hash_password(user_data.password)
    user = UserModel(
        id=str(uuid.uuid4()),
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
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
    for field, value in user_data.model_dump(exclude_unset=True).items():
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


def get_user_by_email(db: Session, user_email: str):
    return db.query(UserModel).filter(UserModel.email == user_email).first()


def login_user(db: Session, login_data: LoginUser):
    user = get_user_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid Credentials')
    token = create_access_token({'sub': user.id})
    return {'access_token': token, 'token_type': 'bearer'}
