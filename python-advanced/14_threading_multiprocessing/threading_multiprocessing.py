# =============================================================
# PYTHON THREADING & MULTIPROCESSING
# =============================================================

# Threading      – multiple threads in ONE process; share memory.
#                  Good for I/O-bound tasks (network, disk).
#                  Limited by the GIL for CPU-bound tasks.
#
# Multiprocessing – multiple OS processes; separate memory spaces.
#                  Good for CPU-bound tasks (computation).
#                  No GIL limitation.
#
# asyncio        – single thread, cooperative multitasking.
#                  Good for many I/O-bound tasks (covered in 07_async_await).

import threading
import multiprocessing
import time
import queue
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# =============================================================
# THREADING – BASICS
# =============================================================

def worker(name: str, delay: float):
    print(f"  [{name}] started  (PID={os.getpid()}, TID={threading.get_ident()})")
    time.sleep(delay)
    print(f"  [{name}] finished after {delay}s")

# Create and start threads
t1 = threading.Thread(target=worker, args=("T1", 0.3))
t2 = threading.Thread(target=worker, args=("T2", 0.2))
t3 = threading.Thread(target=worker, args=("T3", 0.1))

start = time.perf_counter()
t1.start(); t2.start(); t3.start()
t1.join();  t2.join();  t3.join()   # wait for all to finish
print(f"All threads done in {time.perf_counter() - start:.2f}s (expected ~0.3s)")

# =============================================================
# THREAD CLASS (subclassing)
# =============================================================

class DownloadThread(threading.Thread):
    def __init__(self, url: str, delay: float):
        super().__init__(name=f"Downloader-{url}")
        self.url    = url
        self.delay  = delay
        self.result = None

    def run(self):
        time.sleep(self.delay)
        self.result = f"data:{self.url}"

threads = [DownloadThread(f"/item/{i}", delay=0.1) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
    print(f"  {t.name}: {t.result}")

# =============================================================
# THREAD SAFETY – Lock
# =============================================================

# Without a lock, concurrent modifications cause race conditions.
counter = 0
lock    = threading.Lock()

def safe_increment(n: int):
    global counter
    for _ in range(n):
        with lock:            # only one thread at a time
            counter += 1

threads = [threading.Thread(target=safe_increment, args=(1000,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Counter (with lock): {counter}")   # always 5000

# =============================================================
# RLock (re-entrant lock)
# =============================================================

rlock = threading.RLock()

def outer():
    with rlock:
        inner()   # can acquire the same lock again without deadlock

def inner():
    with rlock:
        print("  inner: acquired rlock again (RLock allows this)")

outer()

# =============================================================
# Semaphore – limit concurrent access
# =============================================================

semaphore = threading.Semaphore(3)   # allow max 3 threads at a time

def limited_task(name: str):
    with semaphore:
        print(f"  {name} working")
        time.sleep(0.1)

threads = [threading.Thread(target=limited_task, args=(f"T{i}",)) for i in range(8)]
for t in threads: t.start()
for t in threads: t.join()

# =============================================================
# Event – signal between threads
# =============================================================

event = threading.Event()

def waiter(name: str):
    print(f"  {name} waiting for event...")
    event.wait()                # blocks until event.set()
    print(f"  {name} unblocked!")

def setter():
    time.sleep(0.2)
    print("  Setting event")
    event.set()

threads = [threading.Thread(target=waiter, args=(f"W{i}",)) for i in range(3)]
setter_thread = threading.Thread(target=setter)
for t in threads: t.start()
setter_thread.start()
for t in threads: t.join()
setter_thread.join()

# =============================================================
# Queue – thread-safe producer/consumer
# =============================================================

task_queue   = queue.Queue()
result_queue = queue.Queue()

def producer(q: queue.Queue, items: list):
    for item in items:
        q.put(item)
        print(f"  Produced: {item}")
    q.put(None)   # sentinel

def consumer_worker(task_q: queue.Queue, result_q: queue.Queue):
    while True:
        item = task_q.get()
        if item is None:
            task_q.put(None)   # pass sentinel to other consumers
            break
        result = item ** 2
        result_q.put(result)
        task_q.task_done()

p = threading.Thread(target=producer,         args=(task_queue, list(range(1, 6))))
c = threading.Thread(target=consumer_worker,  args=(task_queue, result_queue))

p.start(); c.start()
p.join();  c.join()

results = []
while not result_queue.empty():
    results.append(result_queue.get())
print(f"Results: {sorted(results)}")   # [1, 4, 9, 16, 25]

# =============================================================
# ThreadPoolExecutor  (easiest way to run threads)
# =============================================================

def fetch_data(url: str) -> str:
    time.sleep(0.1)
    return f"response:{url}"

urls = [f"https://api.example.com/item/{i}" for i in range(10)]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_data, url): url for url in urls}
    for future in as_completed(futures):
        url    = futures[future]
        result = future.result()
        print(f"  {url} → {result}")

# map() style (preserves order)
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch_data, urls[:4]))
    print(results)

# =============================================================
# MULTIPROCESSING – BASICS
# =============================================================

def cpu_task(n: int) -> int:
    """CPU-bound: compute sum of squares up to n."""
    return sum(i ** 2 for i in range(n))

if __name__ == "__main__":   # REQUIRED for multiprocessing on Windows/macOS
    ns = [500_000, 500_000, 500_000, 500_000]

    # Sequential
    start = time.perf_counter()
    results = [cpu_task(n) for n in ns]
    print(f"Sequential:  {time.perf_counter() - start:.2f}s → {results[0]}")

    # Parallel with Pool
    start = time.perf_counter()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_task, ns)
    print(f"Multiprocess:{time.perf_counter() - start:.2f}s → {results[0]}")

    # =============================================================
    # ProcessPoolExecutor  (concurrent.futures interface)
    # =============================================================

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_task, n) for n in ns]
        results = [f.result() for f in futures]
    print(f"Results: {results[0]}")

    # =============================================================
    # INTER-PROCESS COMMUNICATION
    # =============================================================

    # Pipe – two-way communication between two processes
    parent_conn, child_conn = multiprocessing.Pipe()

    def pipe_worker(conn):
        data = conn.recv()
        conn.send(data ** 2)
        conn.close()

    p = multiprocessing.Process(target=pipe_worker, args=(child_conn,))
    p.start()
    parent_conn.send(10)
    print(f"Pipe result: {parent_conn.recv()}")   # 100
    p.join()

    # Queue – for N workers
    mp_queue = multiprocessing.Queue()

    def queue_worker(q: multiprocessing.Queue, value: int):
        q.put(value ** 2)

    processes = [multiprocessing.Process(target=queue_worker, args=(mp_queue, i))
                 for i in range(1, 6)]
    for p in processes: p.start()
    for p in processes: p.join()

    results = [mp_queue.get() for _ in processes]
    print(f"Queue results: {sorted(results)}")   # [1, 4, 9, 16, 25]

    # Shared memory
    shared_value = multiprocessing.Value("i", 0)   # shared integer
    shared_array = multiprocessing.Array("d", [1.0, 2.0, 3.0])

    def modify_shared(val, arr):
        val.value += 100
        for i in range(len(arr)):
            arr[i] *= 2

    p = multiprocessing.Process(target=modify_shared, args=(shared_value, shared_array))
    p.start()
    p.join()
    print(f"Shared value: {shared_value.value}")     # 100
    print(f"Shared array: {list(shared_array)}")     # [2.0, 4.0, 6.0]

# =============================================================
# THREADING vs MULTIPROCESSING vs asyncio
# =============================================================

print("""
                Threading       Multiprocessing   asyncio
Parallelism     Concurrent(GIL) True parallel     Concurrent
Best for        I/O-bound       CPU-bound         I/O-bound (many tasks)
Memory          Shared          Separate          Shared
Overhead        Low             High              Very low
Communication   Shared vars     Queue/Pipe/shmem  await / Queue
GIL limitation  Yes             No                Yes (but rarely matters)

Rule of thumb:
  Many fast I/O tasks     → asyncio
  Blocking I/O tasks      → ThreadPoolExecutor
  CPU-intensive compute   → ProcessPoolExecutor
""")
