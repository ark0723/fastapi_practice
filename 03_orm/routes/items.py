from dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schemas import ItemCreate, ItemUpdate
from typing import Union
import crud_orm

router = APIRouter(prefix="/item", tags=["Items"])


# 전체 아이템 조회
@router.get("/")
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_orm.get_items(db, skip, limit)


# 특정 아이템 조회
@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud_orm.get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return item


@router.post("/")
def create_item(create_item: ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    item = crud_orm.create_item(db, create_item, owner_id)
    return item


@router.put("/{item_id}")
def update_item(item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    item = crud_orm.update_item(db, item_id, item_update)

    if item is None:
        raise HTTPException(status_code=404, detaul="Item not found")
    return item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    is_success = crud_orm.delete_item(db, item_id)

    if not is_success:
        raise HTTPException(status_code=404, detaul="Item not found")
    return {"msg": "Success delete item"}
