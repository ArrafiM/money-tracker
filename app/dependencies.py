from fastapi import Header, HTTPException
from app.middleware import jwtAuth

async def get_token_header(x_token: str = Header(...)):
    auth = jwtAuth.decoded(x_token)
    if auth == "error":
        raise HTTPException(status_code=401, detail="X-Token header invalid")

async def get_token_admin(x_token: str = Header(...)):
    auth = jwtAuth.decoded(x_token)
    if auth == "error":
        raise HTTPException(status_code=401, detail="X-Token header invalid")
    if auth['id_level'] != 1:
        raise HTTPException(status_code=401, detail="Anda tidak berhak mengakses alamat ini")
