from fastapi import HTTPException
from app.database import models


def get_user_by_id(db, user_id):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def get_users(db):
    return db.query(models.User).all()

def delete_user(db, user_id):
    get_user = db.query(models.User).filter(models.User.id == user_id).first()
    if get_user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    get_profile = db.query(models.Profile).filter(models.Profile.user_id == user_id).first()
    if get_profile:
        db.delete(get_profile)
        db.commit()
    db.delete(get_user) 
    db.commit()   
    return {"message":"User Deleted"}