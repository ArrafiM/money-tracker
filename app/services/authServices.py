from passlib.context import CryptContext
from app.database import models
from app.services import mailServices
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt
from decouple import config
from typing import Optional
import random
import string


SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('JWT_EXPIRE'))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def autogenerate(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



generate = autogenerate()
code = f"{generate}"

html = """
<h1>Email verifikasi</h1>
<p> code verifikasi anda dibawah <br>
    <b>{code}</b></p>
""".format(code=code)



async def user_registration(db, user, background_task):
    userCek = db.query(models.User).filter(models.User.email == user.email).first()
    if userCek:
        return {'message':"Email already registered"}
    fake_hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, id_level=user.id_level , code=None)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # sendmail = await mailServices.send_in_background(background_task, email=user.email, html=html)
    return db_user



def login(db, user):
    dataUser = db.query(models.User).filter(models.User.email == user.email).first()
    if dataUser is None:
        raise HTTPException(status_code=404, detail="Email tidak ditemukan")
    if not verify_password(user.password, dataUser.hashed_password):
        raise HTTPException(status_code=404, detail="Password Salah")
    if dataUser.is_verify == False :
        raise HTTPException(status_code=401, detail="Email belum diverifikasi")
    if dataUser.code :
        raise HTTPException(status_code=401, detail="Tidak dapat login, tolong periksa email anda")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    profile = db.query(models.Profile).filter(models.Profile.user_id == dataUser.id).first()
    data = {'id':dataUser.id, 'id_level':dataUser.id_level}
    token = create_access_token(data=data,expires_delta=access_token_expires)
    return {'message':'Berhasil Login','token':token,'id_level':dataUser.id_level}



def email_verification(db, email):
    get_user = db.query(models.User).filter(models.User.email == email.email).first()
    if get_user is None:
        raise HTTPException(status_code=404, detail="Email tidak ditemukan")
    if get_user.code is None:
        raise HTTPException(status_code=403, detail="Email sudah diverifikasi")
    if get_user.code != email.code:
        raise HTTPException(status_code=400, detail="Code tidak sama")
    get_user.code = None
    get_user.is_verify = True
    db.commit()
    db.refresh(get_user)
    return {'message':'Email berhasil diverifikasi'}


async def resend_verification_email(db, email, background_task):
    html_verifikasi = """
    <h1>Email verifikasi</h1>
    <p> code verifikasi anda dibawah <br>
        <b>{}</b></p>
    """.format(code)

    email_url = email.email
    cek_user = db.query(models.User).filter(models.User.email == email_url).first()
    if cek_user is None:
        raise HTTPException(status_code=404, detail="Email tidak ditemukan")
    cek_user.code = code
    db.commit()
    db.refresh(cek_user)
    mailsend = await mailServices.send_in_background(background_task,email=email_url,html=html_verifikasi)
    return mailsend