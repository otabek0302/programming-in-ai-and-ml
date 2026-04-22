# =============================================================
# PYTHON DECORATORS
# =============================================================

# A decorator is a function that takes another function and returns
# a new function with extended behaviour – without modifying the original.
# Syntax:  @decorator  (syntactic sugar for  func = decorator(func))

import functools
import time

# =============================================================
# FUNCTIONS ARE FIRST-CLASS OBJECTS
# =============================================================

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Pass a function as an argument
def apply(func, value):
    return func(value)

print(apply(greet, "Alice"))    # Hello, Alice!
print(apply(str.upper, "hi"))   # HI

# Return a function from a function
def make_greeter(greeting: str):
    def greeter(name: str) -> str:
        return f"{greeting}, {name}!"
    return greeter

hi  = make_greeter("Hi")
hey = make_greeter("Hey")
print(hi("Bob"))    # Hi, Bob!
print(hey("Bob"))   # Hey, Bob!

# =============================================================
# BASIC DECORATOR
# =============================================================

def uppercase(func):
    @functools.wraps(func)   # preserves func's __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))          # HELLO, ALICE!
print(greet.__name__)          # greet  (preserved by @functools.wraps)

# =============================================================
# DECORATOR WITH ARGUMENTS  (decorator factory)
# =============================================================

def repeat(times: int):
    """Decorator factory – returns a decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say(msg: str) -> str:
    return msg

print(say("Hello"))    # ['Hello', 'Hello', 'Hello']

# =============================================================
# PRACTICAL DECORATORS
# =============================================================

# --- Timer ---
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"[{func.__name__}] took {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n: int) -> int:
    return sum(range(n))

slow_sum(1_000_000)

# --- Logger ---
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"  → {result!r}")
        return result
    return wrapper

@log
def add(a: int, b: int) -> int:
    return a + b

add(3, 4)
add(a=10, b=20)

# --- Retry on exception ---
def retry(times: int = 3, exceptions: tuple = (Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"  Attempt {attempt}/{times} failed: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

_call_count = 0

@retry(times=3, exceptions=(ValueError,))
def flaky_function():
    global _call_count
    _call_count += 1
    if _call_count < 3:
        raise ValueError("Not ready yet")
    return "success"

print(flaky_function())

# --- Cache / Memoisation ---
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))   # fast because results are cached

# Python's built-in equivalent (use this in real code)
@functools.lru_cache(maxsize=128)
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

print(fib2(40))
print(fib2.cache_info())

# --- Type validation ---
def validate_types(**type_hints):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig    = inspect.signature(func)
            bound  = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for param_name, value in bound.arguments.items():
                if param_name in type_hints:
                    expected = type_hints[param_name]
                    if not isinstance(value, expected):
                        raise TypeError(
                            f"{param_name} must be {expected.__name__}, "
                            f"got {type(value).__name__}"
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int)
def register(name: str, age: int) -> str:
    return f"Registered {name}, age {age}"

print(register("Alice", 30))

try:
    register("Bob", "thirty")
except TypeError as e:
    print(e)

# =============================================================
# STACKING DECORATORS
# =============================================================

@timer
@log
def multiply(a: int, b: int) -> int:
    return a * b

multiply(6, 7)
# Order: timer wraps log wraps multiply
# Execution: timer → log → multiply

# =============================================================
# CLASS-BASED DECORATORS
# =============================================================

class CountCalls:
    """Counts how many times a function has been called."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func  = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  [{self.func.__name__}] call #{self.count}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

say_hello("Alice")
say_hello("Bob")
say_hello("Carol")
print(f"Called {say_hello.count} times")

# =============================================================
# DECORATOR AS A CLASS  (applied to a class method)
# =============================================================

class classproperty:
    """Read-only class-level property (no built-in support in Python)."""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, owner):
        return self.func(owner)


class Config:
    _debug = False

    @classproperty
    def debug(cls) -> bool:
        return cls._debug


print(Config.debug)   # False

# =============================================================
# functools BUILT-IN DECORATORS  (quick reference)
# =============================================================

# @functools.wraps(func)        – copy metadata from wrapped function
# @functools.lru_cache()        – memoize with LRU eviction
# @functools.cache              – unbounded memoize (Python 3.9+)
# @functools.cached_property    – compute once, store as instance attr
# @functools.total_ordering     – fill in comparison methods from __eq__ + one other
# @functools.singledispatch     – function overloading based on first arg type
# @staticmethod                 – no self/cls
# @classmethod                  – cls instead of self
# @property                     – getter/setter/deleter

from functools import singledispatch

@singledispatch
def process(value):
    print(f"Default: {value!r}")

@process.register(int)
def _(value: int):
    print(f"Int: {value * 2}")

@process.register(str)
def _(value: str):
    print(f"Str: {value.upper()}")

@process.register(list)
def _(value: list):
    print(f"List: {len(value)} items")

process(42)          # Int: 84
process("hello")     # Str: HELLO
process([1, 2, 3])   # List: 3 items
process(3.14)        # Default: 3.14
