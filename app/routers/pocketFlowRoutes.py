from typing import List

from sqlalchemy.orm import Session

from app.controller import pocketFlowController
from app.database import schemas
from app.database.database import engine
from app.database.config import get_db

from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_token_header


router_pocket = APIRouter(
    prefix="/pocket-flow",
    tags=["pocket flow"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router_pocket.post("/", response_model=schemas.PocketFlow)
async def pocket_create(pocket: schemas.PocketFlowCreate, db: Session = Depends(get_db)):
    data = await pocketFlowController.create_pocketFlow(db, pocket)
    return data

@router_pocket.get("/", response_model=List[schemas.PocketFlow])
def get_pocket(db: Session = Depends(get_db)):
    data = pocketFlowController.get_pocketFlow(db)
    return data

@router_pocket.get("/{user_id}", response_model=List[schemas.PocketFlow])
def user_pocketFlow(user_id: int, db: Session = Depends(get_db)):
    data = pocketFlowController.user_pocketFlow(db, user_id)
    return data

@router_pocket.put("-approve/{id}")
async def approve_pocketFlow(id: int, db: Session = Depends(get_db)):
    data = await pocketFlowController.approve_pocketFlow(db,id)
    if data is None:
        raise HTTPException(status_code=404, detail="pocket flow not found")
    return data


