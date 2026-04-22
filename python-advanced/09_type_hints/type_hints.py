# =============================================================
# PYTHON TYPE HINTS  (Static Typing)
# =============================================================

# Type hints annotate variables and functions with expected types.
# Python does NOT enforce them at runtime – they are for:
#   - IDE autocomplete and error detection
#   - Static analysis (mypy, pyright, pytype)
#   - Self-documenting code
#   - Runtime validation libraries (pydantic, beartype)

from __future__ import annotations   # allow forward references everywhere

# =============================================================
# BASIC ANNOTATIONS
# =============================================================

# Variables
name:    str   = "Alice"
age:     int   = 30
height:  float = 1.75
active:  bool  = True
nothing: None  = None

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def no_return(msg: str) -> None:
    print(msg)

print(greet("Bob"))
print(add(3, 4))

# =============================================================
# BUILT-IN COLLECTION TYPES  (Python 3.9+: use lowercase directly)
# =============================================================

def process(items: list[int]) -> dict[str, int]:
    return {"count": len(items), "total": sum(items)}

def lookup(data: dict[str, list[int]], key: str) -> list[int]:
    return data.get(key, [])

print(process([1, 2, 3, 4, 5]))

# Python 3.8 and below required typing module:
# from typing import List, Dict, Tuple, Set
# def process(items: List[int]) -> Dict[str, int]: ...

# =============================================================
# typing MODULE – advanced type forms
# =============================================================

from typing import (
    Any, Union, Optional, Literal, Final,
    Callable, Iterator, Generator, AsyncGenerator,
    TypeVar, Generic, Protocol, overload,
    TYPE_CHECKING,
)

# --- Any ---
def accept_anything(value: Any) -> Any:
    return value

# --- Union – one of several types ---
def stringify(value: int | str) -> str:   # Python 3.10+ syntax
    return str(value)

def old_style(value: Union[int, str]) -> str:   # Python 3.9 and below
    return str(value)

# --- Optional – value or None (= Union[X, None]) ---
def find_user(user_id: int) -> Optional[str]:   # may return None
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(find_user(1))    # Alice
print(find_user(99))   # None

# Python 3.10+ shorthand
def find_user2(user_id: int) -> str | None:
    return None

# --- Literal – exact values only ---
def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"Mode: {mode}")

set_mode("read")
# set_mode("delete")  # mypy would flag this

Direction = Literal["north", "south", "east", "west"]

def move(direction: Direction, steps: int) -> str:
    return f"Moving {direction} {steps} steps"

# --- Final – constant that cannot be reassigned ---
MAX_RETRIES: Final = 3
PI: Final[float] = 3.14159

# --- Callable ---
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(lambda x, y: x + y, 3, 4))   # 7

# No-arg callable returning str
def run(task: Callable[[], str]) -> str:
    return task()

# =============================================================
# TypeVar – generic type variables
# =============================================================

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

def first(items: list[T]) -> T:
    return items[0]

def identity(value: T) -> T:
    return value

print(first([1, 2, 3]))        # 1
print(first(["a", "b", "c"]))  # a

# Constrained TypeVar
Number = TypeVar("Number", int, float)

def double(value: Number) -> Number:
    return value * 2

print(double(5))     # 10
print(double(3.14))  # 6.28

# =============================================================
# Generic CLASSES
# =============================================================

from typing import Generic

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"


int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack)          # Stack([1, 2, 3])
print(int_stack.pop())    # 3
print(int_stack.peek())   # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack)

# =============================================================
# Protocol – structural subtyping (duck typing with types)
# =============================================================

from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...
    def area(self) -> float: ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"○ (r={self.radius})"

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2


class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return f"□ (s={self.side})"

    def area(self) -> float:
        return self.side ** 2


def render(shape: Drawable) -> None:
    print(f"{shape.draw()} – area: {shape.area():.2f}")


render(Circle(5))    # Circle doesn't inherit from Drawable, but satisfies the protocol
render(Square(4))
print(isinstance(Circle(1), Drawable))   # True – runtime_checkable

# =============================================================
# dataclass with type hints
# =============================================================

from dataclasses import dataclass, field

@dataclass
class User:
    name:   str
    email:  str
    age:    int
    tags:   list[str] = field(default_factory=list)
    active: bool = True

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        self.email = self.email.lower()


u = User("Alice", "ALICE@EXAMPLE.COM", 30, tags=["admin"])
print(u)

# =============================================================
# TYPE ALIASES
# =============================================================

# Simple alias
Vector = list[float]
Matrix = list[list[float]]

def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))

print(dot_product([1, 2, 3], [4, 5, 6]))   # 32.0

# NewType – distinct types that don't mix
from typing import NewType

UserId  = NewType("UserId",  int)
OrderId = NewType("OrderId", int)

def get_user(user_id: UserId) -> str:
    return f"user_{user_id}"

uid = UserId(42)
print(get_user(uid))

# =============================================================
# @overload – multiple call signatures
# =============================================================

from typing import overload

@overload
def process(value: int) -> str: ...
@overload
def process(value: str) -> int: ...

def process(value):
    if isinstance(value, int):
        return str(value)
    return len(value)

print(process(42))       # "42"
print(process("hello"))  # 5

# =============================================================
# TYPE_CHECKING – avoid circular imports
# =============================================================

if TYPE_CHECKING:
    from collections.abc import Sequence   # only imported during type checking

# =============================================================
# RUNTIME TYPE CHECKING with get_type_hints
# =============================================================

import typing

def type_checked(func):
    import inspect
    hints = typing.get_type_hints(func)
    sig   = inspect.signature(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        for param, value in bound.arguments.items():
            if param in hints and param != "return":
                expected = hints[param]
                if hasattr(expected, "__origin__"):
                    continue   # skip generic types like list[int]
                if not isinstance(value, expected):
                    raise TypeError(f"{param}: expected {expected.__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper

import functools

@type_checked
def safe_add(a: int, b: int) -> int:
    return a + b

print(safe_add(3, 4))   # 7
try:
    safe_add(3, "4")
except TypeError as e:
    print(e)
