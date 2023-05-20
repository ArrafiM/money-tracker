from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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