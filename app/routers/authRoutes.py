from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from app.database import schemas
from app.database.config import get_db
from sqlalchemy.orm import Session
from app.controller import authControllers

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register', response_model=schemas.Usersend)
async def user_registration(user: schemas.UserCreate, background_task:BackgroundTasks, db: Session = Depends(get_db)):
    data = await authControllers.user_registration(db, user, background_task)
    return data

@router.post("/login")
def login(user:schemas.login, db: Session = Depends(get_db)):
    return authControllers.user_login(db, user)

@router.post("/email-verification")
def email_verification(email:schemas.EmailVerify, db: Session = Depends(get_db)) :
    return authControllers.email_verification(email=email, db=db)

@router.post("/resend-email-verification")
async def resend_verification_email(email:schemas.Email , background_task:BackgroundTasks, db: Session = Depends(get_db)):
    return await authControllers.resend_verification_email(email=email, background_task=background_task, db=db)