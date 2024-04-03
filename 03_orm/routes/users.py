from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_db
from schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session
import crud_orm
from typing import Union

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_orm.create_user(db, user)
    return db_user


# api/v1/user/{user_data} : id 또는 email로 로그인 가능하도록 (문자와 숫자 모두 입력 가능하도록)
@router.get("/{user_data}")
def get_user(user_data: Union[int, str], db: Session = Depends(get_db)):
    try:  # user_data 데이터 타입이 int인 경우
        user_data = int(user_data)
        db_user = crud_orm.get_user_id(db, user_data)
    except:  # user_data 데이터 타입이 str인 경우
        db_user = crud_orm.get_user_email(db, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user


@router.get("/")
def get_users(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud_orm.get_users(db, skip, limit)


@router.put("/{user_id}")
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud_orm.update_user(db, user_id, user_update)

    if updated_user is None:
        raise HTTPException(404, "User Not Found")
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud_orm.delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(404, "User Not Found")
    return deleted_user
