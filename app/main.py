from app.dependencies import get_token_header
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import models
from app.database.database import engine

from app.routers import (
    authRoutes,userRoutes
    )

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Accounts API Docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRoutes.router)
app.include_router(userRoutes.router)
app.include_router(userRoutes.router_user)


@app.get("/")
def read_root():
    return {"Hello": "World"}