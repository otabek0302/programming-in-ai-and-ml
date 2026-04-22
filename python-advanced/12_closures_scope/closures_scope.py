# =============================================================
# PYTHON CLOSURES & SCOPE
# =============================================================

# LEGB Rule – Python's variable lookup order:
#   L – Local      (inside the current function)
#   E – Enclosing  (outer function's scope, for nested functions)
#   G – Global     (module-level)
#   B – Built-in   (Python built-ins: len, print, range, …)

# =============================================================
# LEGB SCOPE LOOKUP
# =============================================================

x = "global"                     # G – global

def outer():
    x = "enclosing"              # E – enclosing

    def inner():
        x = "local"              # L – local
        print(x)                 # local

    inner()
    print(x)                     # enclosing

outer()
print(x)                         # global

# Built-in lookup
print(len([1, 2, 3]))            # B – len is a built-in

# Shadowing a built-in (avoid in real code)
def bad_example():
    len = lambda x: "oops"      # shadows built-in len locally
    return len([1, 2, 3])       # "oops"

print(bad_example())

# =============================================================
# global KEYWORD
# =============================================================

counter = 0

def increment():
    global counter          # declare we want the global, not a local
    counter += 1

increment()
increment()
print(counter)   # 2

# Without global, assignment creates a LOCAL variable
def wrong_increment():
    counter = 0             # this is a NEW local variable
    counter += 1

wrong_increment()
print(counter)   # still 2

# =============================================================
# nonlocal KEYWORD
# =============================================================

def make_counter(start: int = 0, step: int = 1):
    count = start                # enclosing scope variable

    def increment():
        nonlocal count           # refer to enclosing scope's count
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    def get():
        return count

    return increment, reset, get

inc, rst, get = make_counter(start=10, step=5)
print(inc())   # 15
print(inc())   # 20
print(inc())   # 25
rst()
print(get())   # 10

# =============================================================
# CLOSURES
# =============================================================

# A closure is a nested function that "remembers" the enclosing scope's
# variables even after the outer function has returned.

def make_multiplier(factor: float):
    def multiplier(x: float) -> float:
        return x * factor           # factor is "closed over"
    return multiplier               # return the inner function

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Inspect the closure
print(double.__closure__)          # tuple of cell objects
print(double.__closure__[0].cell_contents)   # 2

# =============================================================
# CLOSURE PITFALL – late binding in loops
# =============================================================

# WRONG: all closures share the same variable i
funcs_wrong = [lambda x: x * i for i in range(5)]
print([f(2) for f in funcs_wrong])   # [8, 8, 8, 8, 8]  – all use i=4

# FIX 1: capture i as a default argument
funcs_fixed = [lambda x, i=i: x * i for i in range(5)]
print([f(2) for f in funcs_fixed])   # [0, 2, 4, 6, 8]

# FIX 2: use a factory function to create the closure
def make_func(i):
    return lambda x: x * i

funcs_factory = [make_func(i) for i in range(5)]
print([f(2) for f in funcs_factory])   # [0, 2, 4, 6, 8]

# =============================================================
# PRACTICAL CLOSURES
# =============================================================

# --- Accumulator ---
def make_accumulator(initial: float = 0.0):
    total = initial

    def add(value: float) -> float:
        nonlocal total
        total += value
        return total

    return add

acc = make_accumulator()
print(acc(10))   # 10
print(acc(20))   # 30
print(acc(5))    # 35

# --- Memoisation ---
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache   # expose the cache for inspection
    return wrapper

@memoize
def expensive(n):
    print(f"  computing {n}...")
    return n ** 2

print(expensive(4))   # computing 4... then 16
print(expensive(4))   # 16 – from cache
print(expensive(5))   # computing 5... then 25
print(expensive.cache)

# --- Partial application via closure ---
def partial(func, *partial_args, **partial_kwargs):
    def wrapper(*args, **kwargs):
        return func(*partial_args, *args, **partial_kwargs, **kwargs)
    return wrapper

def greet(greeting, name, punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

hello = partial(greet, "Hello")
print(hello("Alice"))         # Hello, Alice!
print(hello("Bob", "."))      # Hello, Bob.

# =============================================================
# CLASS SCOPE vs FUNCTION SCOPE
# =============================================================

class MyClass:
    value = 10           # class scope – NOT accessible in methods by name alone

    def method(self):
        # print(value)   # NameError – class scope is not in LEGB for methods
        print(self.value)   # must use self.value or MyClass.value

    @classmethod
    def class_method(cls):
        print(cls.value)


MyClass().method()
MyClass.class_method()

# =============================================================
# __slots__ AND __dict__
# =============================================================

class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = Normal(1, 2)
s = Slotted(1, 2)

print(n.__dict__)          # {'x': 1, 'y': 2}
# print(s.__dict__)        # AttributeError – no __dict__ with __slots__

# Memory comparison
import sys
print(sys.getsizeof(n.__dict__))   # 184 bytes (dict overhead)
# Slotted objects are more memory-efficient for many instances

# =============================================================
# VARIABLE SCOPING IN COMPREHENSIONS
# =============================================================

# Python 3: comprehension variables are LOCAL to the comprehension
x = "outer"
result = [x for x in range(5)]   # x inside is local
print(x)      # "outer" – NOT overwritten
print(result) # [0, 1, 2, 3, 4]

# But walrus operator := leaks into enclosing scope
result2 = [y := i * 2 for i in range(3)]
print(y)       # 4 – last assigned value leaks out

# =============================================================
# CLOSURE-BASED STATE MACHINE
# =============================================================

def traffic_light():
    states = ["RED", "GREEN", "YELLOW"]
    index  = 0

    def next_state() -> str:
        nonlocal index
        state = states[index]
        index = (index + 1) % len(states)
        return state

    def current() -> str:
        return states[index]

    return next_state, current

advance, current = traffic_light()
print(current())    # RED
print(advance())    # RED  (then advances)
print(advance())    # GREEN
print(advance())    # YELLOW
print(advance())    # RED  (loops)
print(current())    # GREEN (next state)
