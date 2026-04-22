# =============================================================
# PYTHON GENERATORS & COROUTINES
# =============================================================

# Generator  – function that yields values one at a time (lazy sequence).
# Coroutine  – generator that can also RECEIVE values (two-way communication).

import sys
from typing import Generator, Iterator

# =============================================================
# BASIC GENERATOR FUNCTION
# =============================================================

def count_up(start: int, end: int) -> Generator[int, None, None]:
    current = start
    while current <= end:
        yield current
        current += 1

gen = count_up(1, 5)
print(type(gen))           # <class 'generator'>
print(next(gen))           # 1
print(next(gen))           # 2

for n in count_up(3, 6):
    print(n, end=" ")      # 3 4 5 6
print()

# =============================================================
# GENERATOR PIPELINE  (chaining generators)
# =============================================================

def read_numbers(data: list) -> Iterator[int]:
    for item in data:
        yield item

def filter_even(numbers: Iterator[int]) -> Iterator[int]:
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers: Iterator[int]) -> Iterator[int]:
    for n in numbers:
        yield n ** 2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = square(filter_even(read_numbers(data)))
print(list(pipeline))   # [4, 16, 36, 64, 100]

# =============================================================
# GENERATOR EXPRESSIONS
# =============================================================

gen_expr = (x ** 2 for x in range(10) if x % 2 == 0)
print(list(gen_expr))   # [0, 4, 16, 36, 64]

# Memory comparison
big_list = [x ** 2 for x in range(1_000_000)]
big_gen  = (x ** 2 for x in range(1_000_000))
print(f"List size: {sys.getsizeof(big_list):,} bytes")
print(f"Gen size:  {sys.getsizeof(big_gen)} bytes")   # tiny

del big_list

# =============================================================
# yield FROM  (delegate to a sub-generator)
# =============================================================

def inner():
    yield 1
    yield 2
    yield 3

def outer():
    yield "start"
    yield from inner()          # equivalent to: for x in inner(): yield x
    yield from range(4, 7)
    yield "end"

print(list(outer()))   # ['start', 1, 2, 3, 4, 5, 6, 'end']

# yield from also forwards the return value of the sub-generator
def sub():
    yield 10
    yield 20
    return "sub_done"   # generator return value

def main_gen():
    result = yield from sub()   # captures the StopIteration value
    print(f"Sub returned: {result}")
    yield 30

print(list(main_gen()))   # sub returned: sub_done   [10, 20, 30]

# =============================================================
# INFINITE GENERATORS
# =============================================================

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

import itertools

first_10_fib = list(itertools.islice(fibonacci(), 10))
print(first_10_fib)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def primes() -> Generator[int, None, None]:
    """Infinite generator of prime numbers (sieve-based)."""
    yield 2
    found = [2]
    candidate = 3
    while True:
        if all(candidate % p != 0 for p in found):
            found.append(candidate)
            yield candidate
        candidate += 2

first_15_primes = list(itertools.islice(primes(), 15))
print(first_15_primes)

# =============================================================
# GENERATOR STATE & send()  –  COROUTINES
# =============================================================

# A coroutine is a generator that accepts values via send().
# send(value) resumes the generator AND sets the yield expression to value.

def running_average() -> Generator[float, float, None]:
    """Coroutine that keeps a running average of sent values."""
    total  = 0.0
    count  = 0
    avg    = 0.0
    while True:
        value = yield avg       # yield the current avg AND wait for a new value
        if value is None:
            break
        total += value
        count += 1
        avg = total / count

avg_gen = running_average()
next(avg_gen)             # prime the coroutine (advance to first yield)

print(avg_gen.send(10))   # 10.0
print(avg_gen.send(20))   # 15.0
print(avg_gen.send(30))   # 20.0
print(avg_gen.send(40))   # 25.0

# close() throws GeneratorExit into the coroutine
avg_gen.close()

# =============================================================
# throw()  –  inject an exception into a generator
# =============================================================

def safe_counter():
    count = 0
    while True:
        try:
            yield count
            count += 1
        except ValueError as e:
            print(f"  Resetting counter: {e}")
            count = 0

sc = safe_counter()
print(next(sc))                        # 0
print(next(sc))                        # 1
print(next(sc))                        # 2
sc.throw(ValueError, "manual reset")   # Resetting counter: manual reset
print(next(sc))                        # 0
sc.close()

# =============================================================
# PRACTICAL: CHUNKED FILE READER
# =============================================================

def read_in_chunks(filename: str, chunk_size: int = 64):
    """Yield file content in chunks without loading the whole file."""
    with open(filename, "rb") as f:
        while chunk := f.read(chunk_size):
            yield chunk

# Write a test file
with open("big_file.bin", "wb") as f:
    f.write(b"x" * 256)

total_bytes = sum(len(chunk) for chunk in read_in_chunks("big_file.bin", 64))
print(f"Total bytes read: {total_bytes}")   # 256

import os
os.remove("big_file.bin")

# =============================================================
# PRACTICAL: LAZY CSV READER
# =============================================================

import csv
import io

csv_data = "name,age,city\nAlice,30,Oslo\nBob,25,Paris\nCarol,35,Tokyo\n"

def parse_csv(data: str):
    reader = csv.DictReader(io.StringIO(data))
    for row in reader:
        yield row

for person in parse_csv(csv_data):
    print(f"  {person['name']} ({person['age']}) from {person['city']}")

# =============================================================
# PRACTICAL: DATASTREAM PROCESSOR
# =============================================================

def producer(data: list):
    for item in data:
        yield item

def transformer(source, func):
    for item in source:
        yield func(item)

def consumer(source):
    results = []
    for item in source:
        results.append(item)
    return results

raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = consumer(
    transformer(
        transformer(
            (x for x in raw if x % 2 == 0),   # filter evens
            lambda x: x ** 2                    # square
        ),
        lambda x: x + 1                         # add 1
    )
)
print(result)   # [5, 17, 37, 65, 101]
