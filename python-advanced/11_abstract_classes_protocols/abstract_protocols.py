# =============================================================
# ABSTRACT BASE CLASSES & PROTOCOLS
# =============================================================

# Abstract Base Class (ABC) – defines an interface that subclasses MUST implement.
# Protocol      – structural typing; any class with the right methods qualifies.
#
# ABC  = nominal typing  ("Dog IS-A Animal" via inheritance)
# Protocol = structural typing ("Duck typing with type safety")

from abc import ABC, abstractmethod, abstractproperty
from typing import Protocol, runtime_checkable
import math

# =============================================================
# ABSTRACT BASE CLASS
# =============================================================

class Shape(ABC):
    """Abstract base class – cannot be instantiated directly."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    # Concrete method – available to all subclasses
    def describe(self) -> str:
        return (
            f"{type(self).__name__}: "
            f"area={self.area():.2f}, "
            f"perimeter={self.perimeter():.2f}"
        )


# Shape()   # TypeError: Can't instantiate abstract class Shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)


shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.describe())
    print(isinstance(s, Shape))   # True

# =============================================================
# ABSTRACT PROPERTIES AND CLASS METHODS
# =============================================================

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def sound(self) -> str: ...

    @classmethod
    @abstractmethod
    def habitat(cls) -> str: ...

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"


class Dog(Animal):
    @property
    def sound(self) -> str:
        return "Woof"

    @classmethod
    def habitat(cls) -> str:
        return "Domestic"


class Eagle(Animal):
    @property
    def sound(self) -> str:
        return "Screech"

    @classmethod
    def habitat(cls) -> str:
        return "Mountains"


dog   = Dog("Rex")
eagle = Eagle("Sam")
print(dog.speak())          # Rex says Woof!
print(eagle.speak())        # Sam says Screech!
print(Dog.habitat())        # Domestic
print(Eagle.habitat())      # Mountains

# =============================================================
# PROTOCOL  (structural subtyping / duck typing with types)
# =============================================================

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...
    def area(self) -> float: ...


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def draw(self) -> str:
        return f"△({self.a},{self.b},{self.c})"

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def render_all(shapes: list[Drawable]) -> None:
    for shape in shapes:
        print(f"  {shape.draw()} – area: {shape.area():.2f}")


# Triangle does NOT inherit from Shape or Drawable,
# but satisfies the Drawable Protocol (has draw() and area())
render_all([Circle(3), Rectangle(2, 5), Triangle(3, 4, 5)])

print(isinstance(Triangle(3, 4, 5), Drawable))  # True – runtime_checkable

# =============================================================
# COLLECTIONS ABCs  (built-in abstract interfaces)
# =============================================================

from collections.abc import (
    Sequence, MutableSequence,
    Mapping, MutableMapping,
    Set, MutableSet,
    Iterable, Iterator,
    Callable,
    Hashable, Sized,
)

# Check conformance without subclassing
print(isinstance([1, 2, 3],   Sequence))        # True
print(isinstance((1, 2, 3),   Sequence))        # True
print(isinstance("hello",     Sequence))        # True
print(isinstance({1, 2, 3},   MutableSet))      # True
print(isinstance({"a": 1},    MutableMapping))  # True
print(isinstance(range(10),   Iterable))        # True
print(isinstance(lambda x: x, Callable))        # True
print(isinstance(42,          Hashable))        # True

# =============================================================
# CUSTOM ABSTRACT COLLECTIONS
# =============================================================

class AbstractRepository(ABC):
    """Generic repository interface for data access."""

    @abstractmethod
    def get_by_id(self, id: int): ...

    @abstractmethod
    def get_all(self) -> list: ...

    @abstractmethod
    def save(self, entity) -> None: ...

    @abstractmethod
    def delete(self, id: int) -> bool: ...

    def exists(self, id: int) -> bool:
        return self.get_by_id(id) is not None


class InMemoryUserRepo(AbstractRepository):
    def __init__(self):
        self._store: dict[int, dict] = {}
        self._next_id = 1

    def get_by_id(self, id: int) -> dict | None:
        return self._store.get(id)

    def get_all(self) -> list[dict]:
        return list(self._store.values())

    def save(self, entity: dict) -> None:
        if "id" not in entity:
            entity = {**entity, "id": self._next_id}
            self._next_id += 1
        self._store[entity["id"]] = entity

    def delete(self, id: int) -> bool:
        if id in self._store:
            del self._store[id]
            return True
        return False


repo = InMemoryUserRepo()
repo.save({"name": "Alice", "email": "alice@example.com"})
repo.save({"name": "Bob",   "email": "bob@example.com"})

print(repo.get_all())
print(repo.get_by_id(1))
print(repo.exists(2))   # True
print(repo.exists(99))  # False
repo.delete(1)
print(repo.get_all())

# =============================================================
# MIXIN WITH ABC
# =============================================================

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "Serializable": ...

    def to_json(self) -> str:
        import json
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Serializable":
        import json
        return cls.from_dict(json.loads(json_str))


from dataclasses import dataclass, asdict

@dataclass
class Product(Serializable):
    name:  str
    price: float
    stock: int = 0

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(**data)


p = Product("Laptop", 999.99, 5)
json_str = p.to_json()
print(json_str)

p2 = Product.from_json(json_str)
print(p2)
print(p == p2)   # True

# =============================================================
# ABC vs Protocol – when to use which
# =============================================================

print("""
Use ABC when:
  - You control the class hierarchy
  - Subclasses must inherit from the base
  - You want to provide default implementations
  - You need abstract properties or class methods

Use Protocol when:
  - You don't control the classes (third-party code)
  - You want pure duck typing with type safety
  - You prefer structural over nominal typing
  - Classes don't share a common ancestor but share behaviour
""")
