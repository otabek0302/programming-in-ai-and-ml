# =============================================================
# PYTHON FUNCTIONAL PROGRAMMING
# =============================================================

# Functional programming treats computation as evaluating functions.
# Key ideas:
#   - Pure functions (no side effects)
#   - Immutability
#   - First-class / higher-order functions
#   - Function composition

import functools
import operator
from typing import Callable, TypeVar

T = TypeVar("T")

# =============================================================
# PURE FUNCTIONS
# =============================================================

# Pure: same input → same output, no side effects
def add(a: int, b: int) -> int:
    return a + b

# Impure: mutates external state
total = 0
def impure_add(x):
    global total
    total += x   # side effect!

# =============================================================
# HIGHER-ORDER FUNCTIONS
# =============================================================

def apply_twice(func: Callable, value):
    return func(func(value))

print(apply_twice(lambda x: x * 2, 3))    # 12
print(apply_twice(str.upper, "hello"))     # HELLO  (already upper, no change)
print(apply_twice(lambda s: s + "!", "hi"))  # hi!!

# =============================================================
# map(), filter(), reduce()
# =============================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map – apply a function to every element
squares = list(map(lambda x: x ** 2, nums))
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(operator.add, a, b)))   # [11, 22, 33]

# filter – keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6, 8, 10]

# reduce – cumulatively apply function to produce a single value
total   = functools.reduce(operator.add, nums)
product = functools.reduce(operator.mul, nums)
maximum = functools.reduce(lambda a, b: a if a > b else b, nums)
print(total, product, maximum)   # 55  3628800  10

# reduce with initial value
print(functools.reduce(operator.add, [], 0))   # 0 – safe with empty list

# =============================================================
# PARTIAL FUNCTIONS  –  functools.partial
# =============================================================

# Fix some arguments of a function → create a specialised function
def power(base: float, exp: float) -> float:
    return base ** exp

square  = functools.partial(power, exp=2)
cube    = functools.partial(power, exp=3)
root    = functools.partial(power, exp=0.5)

print(square(4))   # 16.0
print(cube(3))     # 27.0
print(root(16))    # 4.0

# Partial with positional argument
multiply = lambda x, y: x * y
double   = functools.partial(multiply, 2)
triple   = functools.partial(multiply, 3)

print(list(map(double, [1, 2, 3, 4])))   # [2, 4, 6, 8]
print(list(map(triple, [1, 2, 3, 4])))   # [3, 6, 9, 12]

# =============================================================
# FUNCTION COMPOSITION
# =============================================================

def compose(*funcs: Callable) -> Callable:
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))"""
    def composed(value):
        for func in reversed(funcs):
            value = func(value)
        return value
    return composed

def pipe(*funcs: Callable) -> Callable:
    """Compose functions left-to-right: pipe(f, g)(x) == g(f(x))"""
    def piped(value):
        for func in funcs:
            value = func(value)
        return value
    return piped

double  = lambda x: x * 2
inc     = lambda x: x + 1
square  = lambda x: x ** 2

# right-to-left: square first, then double, then inc
f = compose(inc, double, square)
print(f(3))   # inc(double(square(3))) = inc(double(9)) = inc(18) = 19

# left-to-right: square first, then double, then inc
g = pipe(square, double, inc)
print(g(3))   # same result: 19

# =============================================================
# CURRYING
# =============================================================

# Currying = transform f(a, b, c) into f(a)(b)(c)

def curry(func: Callable) -> Callable:
    """Simple currying for 2-arg functions."""
    @functools.wraps(func)
    def curried(a):
        def inner(b):
            return func(a, b)
        return inner
    return curried

@curry
def add(a: int, b: int) -> int:
    return a + b

add5 = add(5)
print(add5(3))   # 8
print(add5(10))  # 15

# More general currying with toolz (or manual implementation)
def multicurry(func: Callable) -> Callable:
    """Curry any function based on its arity."""
    import inspect
    arity = len(inspect.signature(func).parameters)

    def curried(*args):
        if len(args) >= arity:
            return func(*args)
        return lambda *more: curried(*args, *more)
    return curried

@multicurry
def add3(a, b, c):
    return a + b + c

print(add3(1)(2)(3))     # 6
print(add3(1, 2)(3))     # 6
print(add3(1)(2, 3))     # 6
print(add3(1, 2, 3))     # 6

# =============================================================
# CLOSURES
# =============================================================

def counter(start: int = 0, step: int = 1):
    count = start

    def increment():
        nonlocal count
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset

inc, rst = counter(start=10, step=5)
print(inc())   # 15
print(inc())   # 20
print(inc())   # 25
rst()
print(inc())   # 15

# =============================================================
# IMMUTABILITY PATTERNS
# =============================================================

from dataclasses import dataclass, replace

@dataclass(frozen=True)   # frozen = immutable
class Point:
    x: float
    y: float

    def translate(self, dx: float, dy: float) -> "Point":
        return replace(self, x=self.x + dx, y=self.y + dy)

    def scale(self, factor: float) -> "Point":
        return replace(self, x=self.x * factor, y=self.y * factor)


p1 = Point(1, 2)
p2 = p1.translate(3, 4)
p3 = p2.scale(2)

print(p1)   # Point(x=1, y=2)  – unchanged
print(p2)   # Point(x=4, y=6)
print(p3)   # Point(x=8, y=12)

# =============================================================
# itertools – functional building blocks
# =============================================================

import itertools

# chain – flatten iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]

# starmap – map with unpacked arguments
pairs = [(2, 3), (4, 5), (6, 7)]
print(list(itertools.starmap(operator.mul, pairs)))  # [6, 20, 42]

# accumulate – running aggregation
print(list(itertools.accumulate([1, 2, 3, 4, 5])))           # [1, 3, 6, 10, 15]
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))  # [1, 2, 6, 24, 120]

# groupby – group consecutive equal elements
data = sorted([("A", 1), ("B", 2), ("A", 3), ("B", 4)], key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# combinations and permutations
print(list(itertools.combinations("ABC", 2)))     # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.permutations("ABC", 2)))     # all ordered pairs
print(list(itertools.product([0, 1], repeat=3)))  # all 3-bit binary numbers

# compress – filter using a boolean selector
data     = ["a", "b", "c", "d", "e"]
selector = [1, 0, 1, 0, 1]
print(list(itertools.compress(data, selector)))   # ['a', 'c', 'e']

# =============================================================
# PRACTICAL: FUNCTIONAL DATA PIPELINE
# =============================================================

orders = [
    {"id": 1, "product": "Laptop",  "price": 999.99, "qty": 2},
    {"id": 2, "product": "Mouse",   "price":  29.99, "qty": 5},
    {"id": 3, "product": "Monitor", "price": 399.99, "qty": 1},
    {"id": 4, "product": "Keyboard","price":  79.99, "qty": 3},
    {"id": 5, "product": "Headset", "price": 149.99, "qty": 0},
]

pipeline = pipe(
    lambda orders: filter(lambda o: o["qty"] > 0, orders),
    lambda orders: map(lambda o: {**o, "total": o["price"] * o["qty"]}, orders),
    lambda orders: sorted(orders, key=lambda o: o["total"], reverse=True),
    list,
)

results = pipeline(orders)
for o in results:
    print(f"  {o['product']:<12} ${o['total']:>10.2f}")

grand_total = functools.reduce(lambda acc, o: acc + o["total"], results, 0.0)
print(f"  {'TOTAL':<12} ${grand_total:>10.2f}")
