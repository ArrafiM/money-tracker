from jose import JWTError, jwt
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
EXPIRRE = config('JWT_EXPIRE')

def decoded(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except JWTError:
        return 'error'