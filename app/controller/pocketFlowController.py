from app.services import pocketFlowServices


def create_pocketFlow(db, data):
    data = pocketFlowServices.create_pocketFlow(db, data)
    return data

def get_pocketFlow(db):
    data = pocketFlowServices.get_pocketFlow(db)
    return data

def user_pocketFlow(db, user_id):
    data = pocketFlowServices.user_pocketFlow(db,user_id)
    return data

async def approve_pocketFlow(db, id):
    data = await pocketFlowServices.approve_pocketFlow(db,id)
    return data

