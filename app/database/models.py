from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, DateTime, Text
from sqlalchemy.orm import relationship
import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_verify = Column(Boolean, default=True)
    code = Column(String(6))
    id_level = Column(Integer)
    profile = relationship("Profile", back_populates="parent")
    my_pocket = relationship("PocketUser", back_populates="user")



class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(255), index=True)
    lastname = Column(String(255), index=True)
    alamat = Column(String(255))
    kontak = Column(String(15))
    birthday = Column(String(255))
    photo = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))

    parent = relationship("User", back_populates="profile")


class Level(Base):
    __tablename__ = "level"
    id = Column(Integer, primary_key=True, index=True)
    name_level = Column(String(5))

class PocketUser(Base):
    __tablename__ = "pocket_users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    money = Column(BigInteger, default=0)

    user = relationship("User", back_populates="my_pocket")


class PocketFlow(Base):
    __tablename__ = "pocket_flows"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    nominal = Column(BigInteger)
    wallet_id = Column(Integer, ForeignKey("pocket_users.id"))
    is_approve = Column(Boolean, default=False)
    status = Column(String(3))
    approved_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)



