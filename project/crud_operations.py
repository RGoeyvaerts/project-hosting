from fastapi import HTTPException
from sqlalchemy.orm import Session
import auth
import models
import schemas
# import subprocess
# import os


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
    # home_dir = "/home/" + user.email
    # subprocess.run(['sudo', 'useradd', '-m', user.email])
    # subprocess.run(['sudo', 'chpasswd'], input=f"{user.email}:{user.password}", encoding='utf-8')


def set_password(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    user_db = db.query(models.User).filter(
        models.User.email == user.email).first()
    user_db.hashed_password = hashed_password
    db.commit()

    return "success"
