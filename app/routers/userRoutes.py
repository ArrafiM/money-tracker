from typing import List

from sqlalchemy.orm import Session

from app.controller import userControllers
from app.database import schemas
from app.database.config import get_db

from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_token_admin, get_token_header


router_user = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_admin)],
    responses={404: {"description": "Not found"}},
)

@router_user.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userControllers.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=List[schemas.User])
def read_users( db: Session = Depends(get_db)):
    users = userControllers.get_users(db)
    return users

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return userControllers.delete_user(db=db, user_id=user_id)

