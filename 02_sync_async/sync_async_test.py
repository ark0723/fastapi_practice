# 동기와 비동기 차이
from fastapi import APIRouter
import time

router = APIRouter()


@router.get("/slow-sync-ping")
def slow_sync_ping():
    time.sleep(10)

    return {"msg": "pong"}


import asyncio


@router.get("/slow-async-ping")
async def slow_async_ping():  # async 와 await은 단짝
    await asyncio.sleep(10)  # 10초를 기다린다. 근데 다른 작업들은 계속 실행된다
    # 결론: 비동기일때는 waiting이 오래걸리는 작업은 하면 안된다
    return {"msg": "pong"}


# 피보나치
# I/O:  input/output -> 비동기가 좋다
# cpu에 부하가 걸리는 작업(복잡한 연산): 동기가 좋다


def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(35)
    return result


# worst case: cpu부하 -> Event Loop에 부하가 걸림
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {"msg": result}


# good case
# cpu  부하가 많이 걸리는 작업은 -> 이벤트 루프에서 분리후, 별도의 프로세스에서 실행하다록 만들어준다
from concurrent.futures import ProcessPoolExecutor  # 워커접근 가능하게 해줌


def cpu_bound_task():
    with ProcessPoolExecutor as executor:
        result = asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task
        )  # context switching
    return {"result": result}
