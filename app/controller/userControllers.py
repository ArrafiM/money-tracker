from app.services import userServices


def get_user_by_id(db, user_id):
    data = userServices.get_user_by_id(db, user_id)
    return data

def get_users(db):
    data = userServices.get_users(db)
    return data

def delete_user(db, user_id):
    data = userServices.delete_user(db, user_id)
    return data

