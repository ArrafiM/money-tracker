from app.database import models

pocketUser = models.PocketUser

async def create_pocket(db, userId):
    db_pocket = models.PocketUser(user_id=userId)
    db.add(db_pocket)
    db.commit()
    db.refresh(db_pocket)
    return db_pocket

async def get_pocket(db, userId):
    pocket = db.query(pocketUser).filter(pocketUser.user_id == userId).first()
    return pocket

async def update_pocketMoney(db, userId, nominal, status):
    pocket = await get_pocket(db, userId);
    if pocket:
        if status == 'in':
            pocket.money += nominal;
        else:
            pocket.money -= nominal;
        db.add(pocket)
        db.commit()
        db.refresh(pocket)
        return pocket