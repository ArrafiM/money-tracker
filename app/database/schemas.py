from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: Optional[str]
    email: str
    is_active: bool
    id_level: int
    my_pocket: list = []
    # profile: List[Profile] = []

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    id_level: int

class Usersend(BaseModel):
    id: int
    name: Optional[str]
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
    name : Optional[str]
    description: Optional[str]
    nominal: int
    status : str
    is_approve : Optional[bool]

class PocketFlow(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    user_id : int
    is_approve : bool
    status : str
    wallet_id : int
    nominal : int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    approved_at: Optional[datetime]

    class Config:
        orm_mode = True

