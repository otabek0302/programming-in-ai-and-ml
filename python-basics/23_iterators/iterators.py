# =============================================================
# PYTHON ITERATORS
# =============================================================

# An ITERABLE is any object you can loop over (list, tuple, str, dict, set, range).
# An ITERATOR is an object with state that remembers where it is during iteration.
#
# Two special methods (the iterator protocol):
#   __iter__()  – returns the iterator object itself
#   __next__()  – returns the next value; raises StopIteration when done

# =============================================================
# USING iter() AND next()
# =============================================================

fruits = ["apple", "banana", "cherry"]

# Get an iterator from the list
it = iter(fruits)

print(next(it))   # apple
print(next(it))   # banana
print(next(it))   # cherry
# next(it)        # StopIteration – no more items

# Strings are iterable too
it = iter("hello")
print(next(it))   # h
print(next(it))   # e

# A for loop is syntactic sugar for iter() + next() + StopIteration handling
for fruit in fruits:
    print(fruit)

# =============================================================
# WHAT HAPPENS INSIDE A FOR LOOP
# =============================================================

# Python translates:
#   for item in iterable:
#       body
# into roughly:
#   _it = iter(iterable)
#   while True:
#       try:
#           item = next(_it)
#       except StopIteration:
#           break
#       body

# =============================================================
# CUSTOM ITERATOR CLASS
# =============================================================

# Implement __iter__() and __next__() to make any class iterable.

class CountUp:
    """Counts from start up to end (inclusive)."""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self          # the object itself is the iterator

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 5)
for n in counter:
    print(n, end=" ")   # 1 2 3 4 5
print()

# Can also use next() manually
counter = CountUp(10, 13)
print(next(counter))   # 10
print(next(counter))   # 11
print(next(counter))   # 12
print(next(counter))   # 13

# =============================================================
# INFINITE ITERATOR (no StopIteration)
# =============================================================

class InfiniteCounter:
    """Counts up forever from start."""
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value

inf = InfiniteCounter(1)
for i in inf:
    if i > 5:
        break
    print(i, end=" ")   # 1 2 3 4 5
print()

# =============================================================
# GENERATORS  (easiest way to create an iterator)
# =============================================================

# A generator function uses yield instead of return.
# Each call to next() resumes execution after the last yield.
# State is preserved automatically – no class needed.

def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for n in count_up(1, 5):
    print(n, end=" ")   # 1 2 3 4 5
print()

# Generator as a lazy infinite sequence
def natural_numbers(start=1):
    n = start
    while True:
        yield n
        n += 1

gen = natural_numbers()
for _ in range(5):
    print(next(gen), end=" ")   # 1 2 3 4 5
print()

# =============================================================
# GENERATOR EXPRESSIONS  (like list comprehension but lazy)
# =============================================================

# List comprehension – evaluates ALL items immediately
squares_list = [x ** 2 for x in range(10)]

# Generator expression – evaluates items ONE AT A TIME on demand
squares_gen = (x ** 2 for x in range(10))

print(type(squares_list))   # <class 'list'>
print(type(squares_gen))    # <class 'generator'>

print(next(squares_gen))    # 0
print(next(squares_gen))    # 1
print(next(squares_gen))    # 4

# sum() works directly on a generator (no need to build a list first)
total = sum(x ** 2 for x in range(100))
print(total)   # 328350

# Memory comparison
import sys
print(sys.getsizeof(squares_list))              # ~184 bytes
print(sys.getsizeof(x ** 2 for x in range(10))) # 104 bytes – always the same

# =============================================================
# BUILT-IN ITERATORS
# =============================================================

# map(), filter(), zip(), enumerate() all return lazy iterators.

# map
doubled = map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(list(doubled))   # [2, 4, 6, 8, 10]

# filter
evens = filter(lambda x: x % 2 == 0, range(10))
print(list(evens))     # [0, 2, 4, 6, 8]

# zip
pairs = zip([1, 2, 3], ["a", "b", "c"])
print(list(pairs))     # [(1, 'a'), (2, 'b'), (3, 'c')]

# enumerate
for i, val in enumerate(["x", "y", "z"]):
    print(i, val)

# reversed()
for x in reversed([1, 2, 3]):
    print(x, end=" ")   # 3 2 1
print()

# =============================================================
# itertools – powerful iterator tools
# =============================================================

import itertools

# chain – connect multiple iterables
combined = itertools.chain([1, 2], [3, 4], [5])
print(list(combined))   # [1, 2, 3, 4, 5]

# islice – lazy slice of any iterator
gen = natural_numbers()
first_ten = list(itertools.islice(gen, 10))
print(first_ten)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# cycle – repeat an iterable forever
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(colors), end=" ")   # red green blue red green blue red
print()

# count – infinite counter with step
counter = itertools.count(start=0, step=5)
print([next(counter) for _ in range(5)])   # [0, 5, 10, 15, 20]

# takewhile – yield items while condition is True
nums = itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])
print(list(nums))   # [1, 2, 3, 4]

# dropwhile – skip items while condition is True, then yield the rest
nums = itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])
print(list(nums))   # [5, 6, 7]
