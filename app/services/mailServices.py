from fastapi_mail import FastMail, ConnectionConfig, MessageSchema
from app.database import schemas
from decouple import config
from starlette.responses import JSONResponse



conf = ConnectionConfig(
    MAIL_USERNAME=config('SMTP_USERNAME'),
    MAIL_PASSWORD=config('SMTP_PASSWORD'),
    MAIL_PORT=config('SMTP_PORT'),
    MAIL_SERVER=config('SMTP_HOST'),
    MAIL_FROM=config("MAIL_SENDER_EMAIL"),
    MAIL_FROM_NAME=config("MAIL_SENDER_NAME"),
    MAIL_TLS=True,
    MAIL_SSL=False,
)


async def send_in_background(
    background_task,
    email,
    html
    ) -> JSONResponse:
    message = MessageSchema(
        subject="Account digital talent Team",
        recipients=[email],
        body=html,
        subtype="html"
        )

    fm = FastMail(conf)

    background_task.add_task(fm.send_message,message)
    print({"message": "email has been sent"})
    return JSONResponse(status_code=200, content={"message": "email has been sent"})