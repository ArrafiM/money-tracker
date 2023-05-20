from app.services import authServices

async def user_registration(db, user, background_task):
    data = await authServices.user_registration(db, user, background_task)
    return data

def user_login(db, user):
    data = authServices.login(db, user)
    return data

def email_verification(db, email):
    data = authServices.email_verification(db, email)
    return data

async def resend_verification_email(db, email, background_task):
    data = await authServices.resend_verification_email(db, email, background_task)
    return data