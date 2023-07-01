from typing import List, Optional

from sqlalchemy.orm import Session

from app.controller import pocketFlowController
from app.database import schemas
from app.database.database import engine
from app.database.config import get_db

from fastapi import APIRouter, HTTPException, Depends, Query
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
def get_pocket(status: Optional[str] = Query(None, description="(in|out) atau kosongkan untuk get all"), 
               from_date_approved :Optional[str] = Query(None, description="(YYYY-MM-DD) atau kosongkan untuk get all"), 
               to_date_approved : Optional[str] = Query(None, description="(YYYY-MM-DD) atau kosongkan untuk get all"),
               from_date_created :Optional[str] = Query(None, description="(YYYY-MM-DD) atau kosongkan untuk get all"), 
               to_date_created : Optional[str] = Query(None, description="(YYYY-MM-DD) atau kosongkan untuk get all"),
               is_approved: Optional[str] = Query(None, description="(true|false) atau kosongkan untuk get all"),
               user_id: Optional[int] = Query(None, description="(id for user) atau kosongkan untuk get all"),
               db: Session = Depends(get_db)):
    filter = {'from_date_approved':from_date_approved,'to_date_approved':to_date_approved,'status':status,'is_approved':is_approved,
              'from_date_created':from_date_created,'to_date_created':to_date_created, 'user_id':user_id}
    data = pocketFlowController.get_pocketFlow(db,filter)
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


