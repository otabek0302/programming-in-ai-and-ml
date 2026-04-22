# =============================================================
# PYTHON ASYNC / AWAIT  (asyncio)
# =============================================================

# Asynchronous programming lets a single thread handle many tasks
# concurrently by pausing (await) at I/O operations instead of blocking.
#
# Key concepts:
#   coroutine   – async def function, returns a coroutine object
#   event loop  – schedules and runs coroutines
#   await       – suspend execution until an awaitable completes
#   Task        – a coroutine scheduled to run concurrently
#   gather()    – run multiple coroutines concurrently

import asyncio
import time

# =============================================================
# BASIC COROUTINE
# =============================================================

async def greet(name: str) -> str:
    await asyncio.sleep(0.1)   # simulate I/O (non-blocking)
    return f"Hello, {name}!"

# Run a single coroutine
result = asyncio.run(greet("Alice"))
print(result)   # Hello, Alice!

# =============================================================
# SEQUENTIAL vs CONCURRENT
# =============================================================

async def fetch(url: str, delay: float) -> str:
    """Simulate a network request."""
    print(f"  Fetching {url}...")
    await asyncio.sleep(delay)
    print(f"  Done: {url}")
    return f"data from {url}"

# Sequential – each request waits for the previous to finish
async def sequential():
    start = time.perf_counter()
    r1 = await fetch("api/users",    0.3)
    r2 = await fetch("api/products", 0.2)
    r3 = await fetch("api/orders",   0.1)
    elapsed = time.perf_counter() - start
    print(f"Sequential: {elapsed:.2f}s  (expected ~0.6s)")
    return [r1, r2, r3]

# Concurrent – all requests run in parallel
async def concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch("api/users",    0.3),
        fetch("api/products", 0.2),
        fetch("api/orders",   0.1),
    )
    elapsed = time.perf_counter() - start
    print(f"Concurrent: {elapsed:.2f}s  (expected ~0.3s)")
    return results

print("\n--- Sequential ---")
asyncio.run(sequential())

print("\n--- Concurrent ---")
asyncio.run(concurrent())

# =============================================================
# asyncio.create_task()  – fire and forget
# =============================================================

async def background_job(name: str, delay: float):
    await asyncio.sleep(delay)
    print(f"  Background job '{name}' done after {delay}s")
    return name

async def main_with_tasks():
    # Create tasks immediately; they start running in the background
    task1 = asyncio.create_task(background_job("slow",   0.3))
    task2 = asyncio.create_task(background_job("medium", 0.2))
    task3 = asyncio.create_task(background_job("fast",   0.1))

    print("  Tasks created, doing other work...")
    await asyncio.sleep(0.05)
    print("  Still doing other work...")

    # Wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)
    print(f"  Results: {results}")

asyncio.run(main_with_tasks())

# =============================================================
# EXCEPTION HANDLING IN COROUTINES
# =============================================================

async def might_fail(value: int) -> int:
    await asyncio.sleep(0.05)
    if value < 0:
        raise ValueError(f"Negative value: {value}")
    return value * 2

async def handle_errors():
    # Handle individual exceptions
    try:
        result = await might_fail(-1)
    except ValueError as e:
        print(f"  Caught: {e}")

    # gather with return_exceptions=True – exceptions returned as results
    results = await asyncio.gather(
        might_fail(1),
        might_fail(-2),
        might_fail(3),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"  Error: {r}")
        else:
            print(f"  OK: {r}")

asyncio.run(handle_errors())

# =============================================================
# TIMEOUTS
# =============================================================

async def slow_operation():
    await asyncio.sleep(5)
    return "done"

async def with_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.2)
    except asyncio.TimeoutError:
        print("  Timed out!")

asyncio.run(with_timeout())

# =============================================================
# ASYNC CONTEXT MANAGERS
# =============================================================

class AsyncDB:
    async def __aenter__(self):
        print("  Connecting to DB...")
        await asyncio.sleep(0.05)
        print("  Connected")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("  Disconnecting from DB")
        await asyncio.sleep(0.01)
        return False

    async def query(self, sql: str) -> list:
        await asyncio.sleep(0.05)
        return [{"id": 1}, {"id": 2}]

async def use_db():
    async with AsyncDB() as db:
        rows = await db.query("SELECT * FROM users")
        print(f"  Got {len(rows)} rows")

asyncio.run(use_db())

# =============================================================
# ASYNC ITERATORS
# =============================================================

class AsyncCounter:
    def __init__(self, start: int, stop: int):
        self.current = start
        self.stop    = stop

    def __aiter__(self):
        return self

    async def __anext__(self) -> int:
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.01)
        value = self.current
        self.current += 1
        return value

async def use_async_iter():
    async for n in AsyncCounter(1, 6):
        print(n, end=" ")
    print()

asyncio.run(use_async_iter())

# =============================================================
# ASYNC GENERATORS
# =============================================================

async def async_range(start: int, stop: int, delay: float = 0.01):
    for i in range(start, stop):
        await asyncio.sleep(delay)
        yield i

async def use_async_gen():
    results = []
    async for x in async_range(1, 6):
        results.append(x)
    print(results)   # [1, 2, 3, 4, 5]

asyncio.run(use_async_gen())

# =============================================================
# SEMAPHORE  – limit concurrency
# =============================================================

async def limited_fetch(semaphore: asyncio.Semaphore, url: str) -> str:
    async with semaphore:
        await asyncio.sleep(0.1)
        return f"data:{url}"

async def fetch_with_limit():
    sem = asyncio.Semaphore(3)   # max 3 concurrent requests
    urls = [f"/item/{i}" for i in range(10)]
    results = await asyncio.gather(*[limited_fetch(sem, u) for u in urls])
    print(f"Fetched {len(results)} URLs with max 3 concurrent")

asyncio.run(fetch_with_limit())

# =============================================================
# asyncio.Queue  – producer / consumer pattern
# =============================================================

async def producer(queue: asyncio.Queue, items: list):
    for item in items:
        await asyncio.sleep(0.05)
        await queue.put(item)
        print(f"  Produced: {item}")
    await queue.put(None)   # sentinel

async def consumer(queue: asyncio.Queue, results: list):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(0.02)
        results.append(item * 2)
        print(f"  Consumed: {item} → {item * 2}")
        queue.task_done()

async def producer_consumer():
    queue   = asyncio.Queue(maxsize=5)
    results = []
    await asyncio.gather(
        producer(queue, [1, 2, 3, 4, 5]),
        consumer(queue, results),
    )
    print(f"Results: {results}")

asyncio.run(producer_consumer())

# =============================================================
# SYNC vs ASYNC  – quick mental model
# =============================================================

print("""
Synchronous:
  task1 ─────────────►
                        task2 ─────────────►
                                              task3 ─────►

Asynchronous (single thread, concurrent I/O):
  task1 ──┐   ┌─►
  task2 ──┤   ├─►    (all waiting for I/O simultaneously)
  task3 ──┘   └─►

Use async when tasks spend most time WAITING (network, disk, sleep).
Use threads/processes when tasks are CPU-BOUND (computation).
""")
