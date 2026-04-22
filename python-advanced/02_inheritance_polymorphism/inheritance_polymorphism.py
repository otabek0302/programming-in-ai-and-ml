# =============================================================
# PYTHON INHERITANCE & POLYMORPHISM
# =============================================================

# Inheritance  – a child class reuses and extends a parent class.
# Polymorphism – different classes respond to the same interface differently.

# =============================================================
# SINGLE INHERITANCE
# =============================================================

class Animal:
    def __init__(self, name: str, sound: str):
        self.name  = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "Woof")   # call parent __init__
        self.breed = breed

    def fetch(self) -> str:
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self) -> str:
        return f"{self.name} purrrrs..."


dog = Dog("Rex",   "Labrador")
cat = Cat("Luna")

print(dog.speak())    # Rex says Woof!
print(cat.speak())    # Luna says Meow!
print(dog.fetch())    # Rex fetches the ball!
print(cat.purr())     # Luna purrrrs...

# isinstance / issubclass checks
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True  – Dog IS-AN Animal
print(isinstance(dog, Cat))     # False
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# =============================================================
# METHOD OVERRIDING
# =============================================================

class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


import math

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width  = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(shape.describe())

# =============================================================
# POLYMORPHISM  (same interface, different behaviour)
# =============================================================

# total_area works with ANY Shape – no type checks needed.
def total_area(shapes: list) -> float:
    return sum(s.area() for s in shapes)

print(f"Total area: {total_area(shapes):.2f}")

# Duck typing – if it walks like a duck and quacks like a duck…
class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

sq = Square(4)
print(total_area([Circle(3), sq]))   # works even though Square doesn't extend Shape

# =============================================================
# MULTIPLE INHERITANCE
# =============================================================

class Flyable:
    def fly(self) -> str:
        return f"{self.__class__.__name__} is flying"

class Swimmable:
    def swim(self) -> str:
        return f"{self.__class__.__name__} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name: str):
        super().__init__(name, "Quack")

duck = Duck("Donald")
print(duck.speak())   # Donald says Quack!
print(duck.fly())     # Duck is flying
print(duck.swim())    # Duck is swimming

# MRO – Method Resolution Order (C3 linearization)
print(Duck.__mro__)

# =============================================================
# super() AND MRO IN DEPTH
# =============================================================

class A:
    def greet(self) -> str:
        return "Hello from A"

class B(A):
    def greet(self) -> str:
        return "Hello from B, " + super().greet()

class C(A):
    def greet(self) -> str:
        return "Hello from C, " + super().greet()

class D(B, C):
    def greet(self) -> str:
        return "Hello from D, " + super().greet()

d = D()
print(d.greet())   # Hello from D, Hello from B, Hello from C, Hello from A
print(D.__mro__)   # D → B → C → A → object

# =============================================================
# MIXIN PATTERN  (reusable behaviour without deep inheritance)
# =============================================================

class JsonMixin:
    """Add JSON serialisation to any class that has __dict__."""
    import json as _json

    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__, default=str, indent=2)

    @classmethod
    def from_json(cls, json_str: str):
        import json
        return cls(**json.loads(json_str))


class LogMixin:
    """Add simple logging to any class."""
    def log(self, message: str):
        print(f"[{type(self).__name__}] {message}")


class User(JsonMixin, LogMixin):
    def __init__(self, name: str, email: str, age: int):
        self.name  = name
        self.email = email
        self.age   = age


u = User("Alice", "alice@example.com", 30)
print(u.to_json())
u.log("logged in")

# Reconstruct from JSON
json_str = u.to_json()
u2 = User.from_json(json_str)
print(u2.name)

# =============================================================
# ABSTRACT BASE CLASS  (prevent instantiation of base class)
# =============================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, speed: float):
        self.brand = brand
        self.speed = speed

    @abstractmethod
    def fuel_type(self) -> str:
        ...

    @abstractmethod
    def max_range(self) -> float:
        ...

    def describe(self) -> str:
        return (
            f"{self.brand} – fuel: {self.fuel_type()}, "
            f"speed: {self.speed} km/h, range: {self.max_range()} km"
        )


class ElectricCar(Vehicle):
    def __init__(self, brand: str, speed: float, battery_kwh: float):
        super().__init__(brand, speed)
        self.battery_kwh = battery_kwh

    def fuel_type(self) -> str:
        return "Electric"

    def max_range(self) -> float:
        return self.battery_kwh * 6   # rough estimate: 6 km per kWh


class PetrolCar(Vehicle):
    def __init__(self, brand: str, speed: float, tank_liters: float):
        super().__init__(brand, speed)
        self.tank_liters = tank_liters

    def fuel_type(self) -> str:
        return "Petrol"

    def max_range(self) -> float:
        return self.tank_liters * 12   # rough estimate: 12 km per litre


# Vehicle()    # TypeError – cannot instantiate abstract class

tesla  = ElectricCar("Tesla",  250, 100)
toyota = PetrolCar("Toyota",  180, 50)

for v in [tesla, toyota]:
    print(v.describe())
