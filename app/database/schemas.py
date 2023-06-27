from typing import List, Optional

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    email: str
    is_active: bool
    id_level: int
    my_pocket: list = []
    # profile: List[Profile] = []

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    email: str
    password: str
    id_level: int

class Usersend(BaseModel):
    id: int
    email: str
    id_level: str
    hashed_password: str

    class Config:
        orm_mode= True

class login(BaseModel):
    email:str
    password: str

class Email(BaseModel):
    email: str

class EmailVerify(Email):
    code: str

class PocketFlowCreate(BaseModel):
    user_id : int
    is_approve : Optional[bool]
    nominal: int
    status : str

class PocketFlow(BaseModel):
    id: int
    user_id : int
    is_approve : bool
    status : str
    wallet_id : int
    nominal : int

    class Config:
        orm_mode = True

