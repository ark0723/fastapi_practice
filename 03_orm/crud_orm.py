from sqlalchemy.orm import Session
from models import User, Item
import bcrypt
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate


# User -CRUD
def create_user(db: Session, user: UserCreate):
    # print(user.password)  # OAuth2.0
    # user : 유저로부터 받은 데이터(UserCreate 객체)
    encode_pw = user.password.encode("utf-8")
    hashed_password = bcrypt.hashpw(encode_pw, bcrypt.gensalt())

    db_user = User(email=user.email, hashed_password=hashed_password)  # 객체 생성
    db.add(db_user)
    db.commit()

    return db_user  # object -> json


def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def get_users(
    db: Session, skip: int = 0, limit: int = 10
):  # pagination options(skip, limit)
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    user_data = user_update.model_dump()

    for k, v in user_data.items():
        setattr(db_user, k, v)  # update user object: setattr(python inner function)

    db.commit()  # db 저장
    db.refresh(
        db_user
    )  # commit만 하면 db_user는 아직 업데이트전의 객체로 나옴 -> refresh필요

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user


# Item -CRUD
def create_item(db: Session, item: ItemCreate, owner_id: int):
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_item(db: Session, item_id: int):
    # 하나의 아이템 조회
    return db.query(Item).filter(Item.id == item_id).first()


# pagination -> 10개씩 내려주겠다(최신 등록순으로)
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()


def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    # 해당 item객체 조회
    db_item = db.query(Item).filter(Item.id == item_id).first()
    # 해당객체 없을경우
    if not db_item:
        return None
    # 해당 객체 있을경우 -> 객체 update
    item_data = item_update.model_dump()  # dict
    for k, v in item_data.items():
        setattr(db_item, k, v)  # update item object

    db.commit()  # db저장
    db.refresh(
        db_item
    )  # commit만 하면 db_item은 아직 업데이터 전의 객체로 나옴 -> refresh 필요

    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        return None

    db.delete(db_item)
    db.commit()

    return db_item
