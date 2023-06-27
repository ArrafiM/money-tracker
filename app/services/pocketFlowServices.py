from app.database import models
from app.services import walletUserServices
from fastapi import HTTPException
from datetime import datetime

pocketFlow = models.PocketFlow
now = datetime.now()

async def create_pocketFlow(db, data):
    userId = data.user_id
    userPocket = await walletUserServices.get_pocket(db, userId)
    walletId = userPocket.id
    isApprove = data.is_approve or False;
    approvedAt = None
    status = data.status
    if isApprove:
        approvedAt = now
    db_pocket = models.PocketFlow(
        user_id=userId, wallet_id=walletId, is_approve=isApprove, 
        status=status, nominal=data.nominal, approved_at=approvedAt
    )
    if isApprove:
        await walletUserServices.update_pocketMoney(db, userId, nominal=data.nominal, status=status)
    db.add(db_pocket)
    db.commit()
    db.refresh(db_pocket)
    print(db_pocket)
    return db_pocket

def get_pocketFlow(db):
    return db.query(models.PocketFlow).all()

def user_pocketFlow(db, user_id):
    return db.query(pocketFlow).filter(pocketFlow.user_id == user_id).all()

async def approve_pocketFlow(db, id):
    pocketFlowData = db.query(pocketFlow).filter(pocketFlow.id == id).first()
    if pocketFlowData is None : return None
    if pocketFlowData.is_approve == True :
        raise HTTPException(status_code=400, detail="Pocket Flow already approved")
    pocketFlowData.is_approve = True
    pocketFlowData.approved_at = now
    db.add(pocketFlowData)
    db.commit()
    db.refresh(pocketFlowData)
    userId = pocketFlowData.user_id
    status = pocketFlowData.status
    myPocket = await walletUserServices.update_pocketMoney(db, userId, nominal=pocketFlowData.nominal, status=status)
    return myPocket
