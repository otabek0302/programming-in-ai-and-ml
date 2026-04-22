# =============================================================
# PYTHON FOR LOOPS
# =============================================================

# A for loop iterates over any sequence (list, tuple, set, dict, string)
# or any other iterable object.
# Syntax:
#   for variable in iterable:
#       ...

# =============================================================
# LOOP OVER A LIST
# =============================================================

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# =============================================================
# LOOP OVER A STRING  (iterates character by character)
# =============================================================

for char in "banana":
    print(char)

# =============================================================
# BREAK – exit the loop early
# =============================================================

# Stop when item is "banana".
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
# prints: apple, banana

# Break BEFORE the print – "banana" itself is not printed.
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
# prints: apple

# =============================================================
# CONTINUE – skip to the next iteration
# =============================================================

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# prints: apple, cherry

# =============================================================
# ELSE – runs once after the loop finishes normally (no break)
# =============================================================

for fruit in fruits:
    print(fruit)
else:
    print("Loop finished")   # always runs here (no break)

# Else is skipped when break fires:
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
else:
    print("This will NOT print")

# =============================================================
# PASS – empty loop body placeholder
# =============================================================

for fruit in fruits:
    pass    # valid, does nothing; avoids IndentationError

# =============================================================
# range() – generate a sequence of numbers
# =============================================================

# range(stop)              – 0 up to (not including) stop
for x in range(6):
    print(x)               # 0 1 2 3 4 5

# range(start, stop)       – start up to (not including) stop
for x in range(2, 6):
    print(x)               # 2 3 4 5

# range(start, stop, step) – custom step
for x in range(2, 30, 3):
    print(x)               # 2 5 8 11 14 17 20 23 26 29

# Counting down
for x in range(10, 0, -2):
    print(x)               # 10 8 6 4 2

# =============================================================
# LOOP OVER A LIST WITH INDEX using range() + len()
# =============================================================

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# =============================================================
# enumerate() – get both index and value cleanly
# =============================================================

for i, fruit in enumerate(fruits):
    print(i, fruit)

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# =============================================================
# LOOP OVER A TUPLE
# =============================================================

colors = ("red", "green", "blue")
for color in colors:
    print(color)

# =============================================================
# LOOP OVER A DICTIONARY
# =============================================================

person = {"name": "John", "age": 36, "city": "Oslo"}

# Keys only (default)
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# =============================================================
# LOOP OVER A SET
# =============================================================

# Order is not guaranteed with sets.
fruits_set = {"apple", "banana", "cherry"}
for fruit in fruits_set:
    print(fruit)

# =============================================================
# NESTED FOR LOOPS
# =============================================================

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        print(a, f)

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# =============================================================
# zip() – loop over two iterables at once
# =============================================================

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip stops at the shortest iterable
a = [1, 2, 3]
b = ["x", "y"]
for x, y in zip(a, b):
    print(x, y)    # (1, x), (2, y) – 3 is dropped

# =============================================================
# LIST COMPREHENSION (compact for loop → new list)
# =============================================================

# Syntax: [expression for item in iterable if condition]

squares = [x ** 2 for x in range(1, 6)]
print(squares)    # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)      # [0, 2, 4, 6, 8]

upper_fruits = [f.upper() for f in fruits]
print(upper_fruits)

# Nested comprehension (flatten a 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Find first even number ---
numbers = [1, 3, 7, 4, 9, 2]
for n in numbers:
    if n % 2 == 0:
        print(f"First even: {n}")
        break

# --- Collect matching items ---
words = ["sky", "sea", "sun", "moon", "star", "sand"]
s_words = [w for w in words if w.startswith("s")]
print(s_words)   # ['sky', 'sea', 'sun', 'star', 'sand']

# --- FizzBuzz ---
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
