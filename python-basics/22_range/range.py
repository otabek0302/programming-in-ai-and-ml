# =============================================================
# PYTHON range()
# =============================================================

# range() generates an immutable sequence of numbers.
# It does NOT store all values in memory – it generates on demand (lazy).
# Syntax:
#   range(stop)
#   range(start, stop)
#   range(start, stop, step)

# =============================================================
# BASIC FORMS
# =============================================================

# range(stop) – 0 up to (not including) stop
r = range(6)
print(r)            # range(0, 6)  – not the numbers, just the range object
print(list(r))      # [0, 1, 2, 3, 4, 5]
print(type(r))      # <class 'range'>

# range(start, stop)
print(list(range(2, 7)))     # [2, 3, 4, 5, 6]
print(list(range(0, 1)))     # [0]
print(list(range(5, 5)))     # []  – empty when start == stop

# range(start, stop, step)
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(range(0, 10, 3)))   # [0, 3, 6, 9]
print(list(range(1, 20, 4)))   # [1, 5, 9, 13, 17]

# =============================================================
# COUNTING DOWN  (negative step)
# =============================================================

print(list(range(10, 0, -1)))    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 0, -2)))    # [10, 8, 6, 4, 2]
print(list(range(5, -1, -1)))    # [5, 4, 3, 2, 1, 0]

# =============================================================
# range() IN FOR LOOPS
# =============================================================

for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4
print()

for i in range(1, 6):
    print(i, end=" ")   # 1 2 3 4 5
print()

# Loop n times
n = 4
for _ in range(n):      # _ is convention for "unused variable"
    print("hello")

# Loop with index over a list
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# =============================================================
# range() PROPERTIES
# =============================================================

r = range(0, 20, 2)

# Membership test (O(1) – much faster than checking a list)
print(10 in r)    # True
print(11 in r)    # False

# Length
print(len(r))     # 10

# Indexing
print(r[0])       # 0
print(r[-1])      # 18

# Slicing (returns a new range)
print(r[2:5])           # range(4, 10, 2)
print(list(r[2:5]))     # [4, 6, 8]

# Reversed
print(list(reversed(r)))  # [18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

# =============================================================
# CONVERTING range() TO OTHER TYPES
# =============================================================

print(list(range(5)))           # [0, 1, 2, 3, 4]
print(tuple(range(5)))          # (0, 1, 2, 3, 4)
print(set(range(5)))            # {0, 1, 2, 3, 4}

# =============================================================
# MEMORY EFFICIENCY
# =============================================================

import sys

# A range object uses the same tiny amount of memory regardless of size.
small = range(10)
large = range(10_000_000)
print(sys.getsizeof(small))   # 48 bytes
print(sys.getsizeof(large))   # 48 bytes  – same!

# A list grows with its size.
small_list = list(range(10))
large_list = list(range(10_000))
print(sys.getsizeof(small_list))   # ~184 bytes
print(sys.getsizeof(large_list))   # ~87624 bytes

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Sum of 1 to 100 ---
print(sum(range(1, 101)))      # 5050

# --- Even numbers up to 20 ---
print(list(range(0, 21, 2)))   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# --- Multiplication table ---
for i in range(1, 6):
    row = [i * j for j in range(1, 6)]
    print(row)

# --- Reverse a list using range ---
items = ["a", "b", "c", "d"]
for i in range(len(items) - 1, -1, -1):
    print(items[i], end=" ")
print()

# --- Repeat something n times ---
def repeat(value, n):
    return [value for _ in range(n)]

print(repeat("hi", 4))    # ['hi', 'hi', 'hi', 'hi']

# --- Generate indices for batching ---
data = list(range(100))
batch_size = 10
for start in range(0, len(data), batch_size):
    batch = data[start:start + batch_size]
    print(f"Batch {start // batch_size}: {batch}")
