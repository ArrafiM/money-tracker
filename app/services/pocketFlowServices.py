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
        status=status, nominal=data.nominal, approved_at=approvedAt,
        name=data.name or None, description=data.description or None
    )
    if isApprove:
        await walletUserServices.update_pocketMoney(db, userId, nominal=data.nominal, status=status)
    db.add(db_pocket)
    db.commit()
    db.refresh(db_pocket)
    print(db_pocket)
    return db_pocket

def get_pocketFlow(db,filter):
    from_date_approved = filter['from_date_approved'] or None
    to_date_approved = filter['to_date_approved'] or None
    status = filter['status'] or None
    is_approved = filter['is_approved'] or None
    from_date_created = filter['from_date_created'] or None
    to_date_created = filter['to_date_created'] or None
    data  = db.query(models.PocketFlow)
    if status:
        data = data.filter(models.PocketFlow.status == status)
    if is_approved in ['true', 'false']:
        data = data.filter(models.PocketFlow.is_approve == is_approved)
    if to_date_approved and from_date_approved:
        from_date_approved_obj = datetime.strptime(from_date_approved, "%Y-%m-%d")
        to_date_approved_obj = datetime.strptime(to_date_approved, "%Y-%m-%d")
        data = data.filter(models.PocketFlow.approved_at.between(from_date_approved_obj, to_date_approved_obj))
    if to_date_created and from_date_created:
        from_date_created_obj = datetime.strptime(from_date_created, "%Y-%m-%d")
        to_date_created_obj = datetime.strptime(to_date_created, "%Y-%m-%d")
        data = data.filter(models.PocketFlow.created_at.between(from_date_created_obj, to_date_created_obj))
    return data.all()

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
