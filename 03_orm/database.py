from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base, as_declarative

from datetime import datetime
from sqlalchemy import Column, DateTime

# 동기용 DB 접속 명령어 (pymysql 사용)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:kr14021428@localhost/oz-fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 DB 접속(aiomysql 사용)
# 무거운 작업(I/O)요청(5초짜리)이 먼저와도, 뒤에 가벼운  I/O 작업 요청(1초짜리)이 들어오면 더 빨리 끝나는 녀석이 응답된다
ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:kr14021428@localhost/oz-fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)


# @as_declarative()
# class Base:
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     __name__: str


Base = declarative_base()
