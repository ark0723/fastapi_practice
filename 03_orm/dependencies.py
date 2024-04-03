from database import SessionLocal, AsyncSessionLocal


# 동기용
def get_db():
    db = SessionLocal()
    try:
        yield db  # generator : 연결된 상태를 유지시켜준다
    finally:
        db.close()


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
