from pydantic import BaseModel
from typing import List


# schemas / item.py
# schemas / user.py


# pydantic -> 데이터 유효성 검증
class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # orm 방식으로 데이터 필드 읽기가 가능


class UserBase(BaseModel):  # email을 따로 빼내어 기본 모델로 지정후 User에 상속
    email: str


class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        from_attributes = True  # orm 방식으로 데이터 필드 읽기가 가능


class UserCreate(UserBase):
    # 유저가입시 이메일과 비밀번호 필요
    # UserBase모델은 이메일 validation이미 하므로 password만 받으면 됨
    password: str


class UserUpdate(
    UserBase
):  # 유저 id는 변경불가, 이메일과 비번은 업데이트 가능이라면(정책설정)
    email: str | None = None  # v3.10부터 등장
    # emai: Optional[str] = None # v.3.10이전
    password: str | None = None
