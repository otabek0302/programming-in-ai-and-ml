# =============================================================
# PYTHON LAMBDA
# =============================================================

# A lambda is a small, anonymous (nameless) function.
# Can take any number of arguments but has only ONE expression.
# The expression is evaluated and returned automatically.
# Syntax:
#   lambda arguments : expression

# =============================================================
# BASIC LAMBDA
# =============================================================

# Equivalent to:
#   def add10(x):
#       return x + 10
add10 = lambda x: x + 10
print(add10(5))    # 15
print(add10(20))   # 30

# Multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))   # 12

# Three arguments
full_name = lambda first, middle, last: f"{first} {middle} {last}"
print(full_name("John", "Paul", "Smith"))

# =============================================================
# WHY USE LAMBDA?
# =============================================================

# Lambda shines when you need a short, throw-away function
# as an argument to another function (like sorted, map, filter, reduce).
# Using def for these one-liners would be unnecessarily verbose.

# =============================================================
# LAMBDA INSIDE A FUNCTION (factory pattern)
# =============================================================

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
times10 = make_multiplier(10)

print(double(5))    # 10
print(triple(5))    # 15
print(times10(5))   # 50

# =============================================================
# LAMBDA WITH sorted()
# =============================================================

# Sort a list of tuples by the second element
pairs = [(1, "banana"), (3, "apple"), (2, "cherry")]
pairs_sorted = sorted(pairs, key=lambda item: item[1])
print(pairs_sorted)   # [(3, 'apple'), (1, 'banana'), (2, 'cherry')]

# Sort a list of dicts by a field
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 35},
]
by_age = sorted(people, key=lambda p: p["age"])
for p in by_age:
    print(p)

# Sort strings by length
words = ["banana", "apple", "kiwi", "cherry", "fig"]
print(sorted(words, key=lambda w: len(w)))

# Sort with multiple criteria (age, then name)
by_age_name = sorted(people, key=lambda p: (p["age"], p["name"]))
for p in by_age_name:
    print(p)

# =============================================================
# LAMBDA WITH map()
# =============================================================

# map(function, iterable) – apply function to every item, returns an iterator.
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10]

# map() with two iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)   # [11, 22, 33]

# Convert strings to uppercase
words = ["hello", "world", "python"]
upper = list(map(lambda w: w.upper(), words))
print(upper)   # ['HELLO', 'WORLD', 'PYTHON']

# =============================================================
# LAMBDA WITH filter()
# =============================================================

# filter(function, iterable) – keep only items where function returns True.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)    # [1, 3, 5, 7, 9]

above_five = list(filter(lambda x: x > 5, numbers))
print(above_five)   # [6, 7, 8, 9, 10]

# Filter strings by length
words = ["hi", "hello", "hey", "howdy", "yo"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)   # ['hello', 'howdy']

# =============================================================
# LAMBDA WITH reduce()
# =============================================================

# reduce(function, iterable) – cumulatively apply function to items.
# Not built-in; must import from functools.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)    # 15   (((((1+2)+3)+4)+5))

product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120

maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 5

# =============================================================
# LAMBDA vs DEF – when to use which
# =============================================================

# Use LAMBDA when:
#   - The function is short (one expression)
#   - It is used only once or as an inline argument
#   - You don't need a docstring or complex logic

# Use DEF when:
#   - The function has multiple lines or statements
#   - You need a docstring
#   - The function is reused in multiple places
#   - Readability matters more than brevity

# Lambda – concise but less readable for complex logic:
process = lambda x: x ** 2 if x > 0 else 0

# def – clearer for the same logic:
def process_v2(x):
    """Return x squared if positive, else 0."""
    if x > 0:
        return x ** 2
    return 0

print(process(4))     # 16
print(process(-3))    # 0
print(process_v2(4))  # 16
