# =============================================================
# PYTHON DATACLASSES
# =============================================================

# dataclasses auto-generate boilerplate (__init__, __repr__, __eq__, etc.)
# based on annotated class variables.

from dataclasses import (
    dataclass, field, fields, asdict, astuple,
    replace, make_dataclass, KW_ONLY, InitVar,
)
from typing import ClassVar, Optional
import json

# =============================================================
# BASIC DATACLASS
# =============================================================

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
p3 = Point(3.0, 4.0)

print(p1)          # Point(x=1.0, y=2.0)   – free __repr__
print(p1 == p2)    # True                   – free __eq__ (compares fields)
print(p1 == p3)    # False

# =============================================================
# DEFAULT VALUES
# =============================================================

@dataclass
class Config:
    host:    str   = "localhost"
    port:    int   = 8080
    debug:   bool  = False
    timeout: float = 30.0

c = Config()
print(c)   # Config(host='localhost', port=8080, debug=False, timeout=30.0)

c2 = Config(host="example.com", port=443, debug=True)
print(c2)

# =============================================================
# field()  –  fine-grained control
# =============================================================

@dataclass
class User:
    name:        str
    email:       str
    age:         int
    tags:        list[str]         = field(default_factory=list)
    _id:         int               = field(default=0, repr=False)  # hidden in repr
    password:    str               = field(default="", repr=False, compare=False)

    # ClassVar is NOT a dataclass field
    _count: ClassVar[int] = 0

    def __post_init__(self):
        User._count += 1
        self._id = User._count
        self.email = self.email.lower()
        if self.age < 0:
            raise ValueError(f"Invalid age: {self.age}")


u1 = User("Alice", "ALICE@EXAMPLE.COM", 30, tags=["admin"])
u2 = User("Bob",   "bob@example.com",   25)

print(u1)            # User(name='Alice', email='alice@example.com', age=30, tags=['admin'])
print(u1._id)        # 1
print(u2._id)        # 2
print(User._count)   # 2

# =============================================================
# FROZEN DATACLASS  (immutable)
# =============================================================

@dataclass(frozen=True)
class Coordinate:
    latitude:  float
    longitude: float

    def distance_to(self, other: "Coordinate") -> float:
        return ((self.latitude - other.latitude) ** 2 +
                (self.longitude - other.longitude) ** 2) ** 0.5


oslo  = Coordinate(59.91, 10.75)
paris = Coordinate(48.85, 2.35)

print(oslo)
print(oslo.distance_to(paris))

# oslo.latitude = 0   # FrozenInstanceError

# frozen dataclasses are hashable → can be dict keys / set members
locations = {oslo: "home", paris: "office"}
print(locations[oslo])

# =============================================================
# replace()  –  create modified copy of a frozen dataclass
# =============================================================

p = Point(1.0, 2.0)
q = replace(p, y=99.0)
print(p)   # Point(x=1.0, y=2.0)   – unchanged
print(q)   # Point(x=1.0, y=99.0)

# =============================================================
# POST-INIT PROCESSING  –  __post_init__
# =============================================================

@dataclass
class Rectangle:
    width:    float
    height:   float
    area:     float = field(init=False)      # computed, not a constructor arg
    diagonal: float = field(init=False, repr=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area     = self.width * self.height
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5


r = Rectangle(3.0, 4.0)
print(r)            # Rectangle(width=3.0, height=4.0, area=12.0)
print(r.diagonal)   # 5.0

# =============================================================
# InitVar – parameter used only in __post_init__, not stored
# =============================================================

@dataclass
class HashedPassword:
    username: str
    _hashed:  str = field(init=False, repr=False)
    password: InitVar[str] = ""   # accepted in constructor, not stored

    def __post_init__(self, password: str):
        import hashlib
        self._hashed = hashlib.sha256(password.encode()).hexdigest()[:16]

    def verify(self, password: str) -> bool:
        import hashlib
        return self._hashed == hashlib.sha256(password.encode()).hexdigest()[:16]


hp = HashedPassword("alice", password="secret123")
print(hp)                         # HashedPassword(username='alice')
print(hp.verify("secret123"))     # True
print(hp.verify("wrong"))         # False

# =============================================================
# ORDERING  (order=True)
# =============================================================

@dataclass(order=True)
class Product:
    sort_index: float = field(init=False, repr=False)
    name:       str   = field(compare=False)
    price:      float

    def __post_init__(self):
        self.sort_index = self.price   # sort by price


products = [
    Product("Laptop",   999.99),
    Product("Mouse",     29.99),
    Product("Monitor",  399.99),
    Product("Keyboard",  79.99),
]

print(sorted(products))   # sorted by price
print(min(products))
print(max(products))

# =============================================================
# INHERITANCE WITH DATACLASSES
# =============================================================

@dataclass
class Animal:
    name:  str
    sound: str

@dataclass
class Dog(Animal):
    breed: str
    age:   int = 0

    def bark(self) -> str:
        return f"{self.name} ({self.breed}) says {self.sound}!"

rex = Dog("Rex", "Woof", "Labrador", age=3)
print(rex)
print(rex.bark())

# =============================================================
# UTILITY FUNCTIONS
# =============================================================

@dataclass
class Person:
    name:  str
    age:   int
    email: str

p = Person("Alice", 30, "alice@example.com")

# fields() – inspect dataclass fields
for f in fields(p):
    print(f"  {f.name}: {f.type} = {getattr(p, f.name)!r}")

# asdict() – convert to dict (recursive)
d = asdict(p)
print(d)   # {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# astuple() – convert to tuple (recursive)
t = astuple(p)
print(t)   # ('Alice', 30, 'alice@example.com')

# JSON serialisation
print(json.dumps(asdict(p), indent=2))

# =============================================================
# make_dataclass()  –  create dataclass dynamically
# =============================================================

FlexPoint = make_dataclass("FlexPoint", [("x", float), ("y", float), ("z", float, 0.0)])
fp = FlexPoint(1.0, 2.0)
print(fp)   # FlexPoint(x=1.0, y=2.0, z=0.0)

# =============================================================
# KW_ONLY  (Python 3.10+)  – force keyword-only fields
# =============================================================

@dataclass
class Server:
    host: str
    port: int
    _:    KW_ONLY          # all fields after this are keyword-only
    debug:   bool  = False
    timeout: float = 30.0

s = Server("localhost", 8080, debug=True)
print(s)

# =============================================================
# DATACLASS vs NamedTuple vs dict
# =============================================================

from collections import namedtuple
from typing import NamedTuple

# namedtuple (immutable, lightweight)
PersonTuple = namedtuple("PersonTuple", ["name", "age"])
pt = PersonTuple("Alice", 30)

# typing.NamedTuple (typed namedtuple)
class TypedPerson(NamedTuple):
    name:  str
    age:   int
    email: str = ""

tp = TypedPerson("Bob", 25)
print(tp)

# Use dataclass when:
#   - You need mutability, methods, inheritance
#   - You want fine-grained field control (repr, compare, hash)
# Use NamedTuple when:
#   - Immutable, needs to be a tuple (CSV rows, return values)
# Use dict when:
#   - Dynamic keys, schema not known at code time
