# =============================================================
# PYTHON CLASSES & OBJECTS
# =============================================================

# A class is a blueprint for creating objects.
# An object is an instance of a class.
# OOP organises code around data (attributes) and behaviour (methods).

# =============================================================
# DEFINING A CLASS
# =============================================================

class Dog:
    # Class attribute – shared by ALL instances
    species = "Canis lupus familiaris"

    # __init__ is the constructor – called when creating an instance
    def __init__(self, name: str, age: int):
        # Instance attributes – unique to each instance
        self.name = name
        self.age  = age

    # Instance method – first parameter is always self
    def bark(self) -> str:
        return f"{self.name} says: Woof!"

    def description(self) -> str:
        return f"{self.name} is {self.age} years old."

    # __str__ – human-readable string representation (used by print())
    def __str__(self) -> str:
        return f"Dog(name={self.name!r}, age={self.age})"

    # __repr__ – unambiguous representation (used in REPL and repr())
    def __repr__(self) -> str:
        return f"Dog({self.name!r}, {self.age})"


# Creating instances
dog1 = Dog("Rex",   3)
dog2 = Dog("Bella", 5)

print(dog1)                   # Dog(name='Rex', age=3)
print(dog1.bark())            # Rex says: Woof!
print(dog1.description())     # Rex is 3 years old.
print(dog2.name)              # Bella
print(Dog.species)            # Canis lupus familiaris
print(dog1.species)           # accessible from instance too

# =============================================================
# MODIFYING & DELETING ATTRIBUTES
# =============================================================

dog1.age = 4             # modify
print(dog1.age)          # 4

dog1.color = "brown"     # add new attribute dynamically
print(dog1.color)        # brown

del dog1.color           # delete attribute
# print(dog1.color)      # AttributeError

# =============================================================
# CLASS METHOD  –  @classmethod
# =============================================================

# Receives the CLASS (cls) as first argument, not an instance.
# Can modify class state; used as alternative constructors.

class Person:
    population = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """Alternative constructor: create Person from birth year."""
        import datetime
        age = datetime.date.today().year - birth_year
        return cls(name, age)

    @classmethod
    def get_population(cls) -> int:
        return cls.population

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"


p1 = Person("Alice", 30)
p2 = Person.from_birth_year("Bob", 1995)
print(p1)                       # Alice (30)
print(p2)                       # Bob (age calculated)
print(Person.get_population())  # 2

# =============================================================
# STATIC METHOD  –  @staticmethod
# =============================================================

# No access to cls or self – it's just a utility function
# that logically belongs to the class.

class MathUtils:
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def clamp(value: float, lo: float, hi: float) -> float:
        """Clamp value to the range [lo, hi]."""
        return max(lo, min(value, hi))


print(MathUtils.is_prime(17))        # True
print(MathUtils.is_prime(18))        # False
print(MathUtils.clamp(150, 0, 100))  # 100
print(MathUtils.clamp(-5,  0, 100))  # 0

# =============================================================
# PROPERTIES  –  @property
# =============================================================

# Properties let you use attribute syntax while running getter/setter logic.

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius    # _ prefix = "private by convention"

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5 / 9   # validates via celsius setter

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    def __str__(self) -> str:
        return f"{self._celsius}°C / {self.fahrenheit}°F / {self.kelvin}K"


t = Temperature(100)
print(t)                   # 100°C / 212.0°F / 373.15K

t.celsius = 0
print(t)                   # 0°C / 32.0°F / 273.15K

t.fahrenheit = 212
print(t.celsius)           # 100.0

try:
    t.celsius = -300
except ValueError as e:
    print(e)               # Temperature below absolute zero!

# =============================================================
# ENCAPSULATION  (name mangling for truly private attributes)
# =============================================================

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner    = owner
        self.__balance = balance    # __ prefix = name-mangled (_BankAccount__balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"Account({self.owner!r}, balance={self.__balance:.2f})"


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)                      # Account('Alice', balance=1300.00)
print(acc.balance)              # 1300.0
# print(acc.__balance)          # AttributeError – name-mangled
print(acc._BankAccount__balance) # 1300.0 – accessible if you really need it

# =============================================================
# SLOTS  –  memory-efficient classes
# =============================================================

# __slots__ prevents arbitrary attribute creation and saves memory
# by replacing the instance __dict__ with a fixed-size structure.
# Useful when creating millions of small objects.

class Point:
    __slots__ = ("x", "y")   # only these attributes are allowed

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p2.distance_to(p1))   # 5.0
# p1.z = 1                  # AttributeError – z not in __slots__

# =============================================================
# PRACTICAL EXAMPLE – Product catalogue
# =============================================================

class Product:
    _next_id = 1

    def __init__(self, name: str, price: float, stock: int = 0):
        self.id    = Product._next_id
        Product._next_id += 1
        self.name  = name
        self._price = price
        self.stock  = stock

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(data["name"], data["price"], data.get("stock", 0))

    def is_available(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        status = "In stock" if self.is_available() else "Out of stock"
        return f"[{self.id}] {self.name} – ${self.price:.2f} ({status})"


p1 = Product("Laptop", 999.99, 5)
p2 = Product.from_dict({"name": "Mouse", "price": 29.99, "stock": 0})

for p in [p1, p2]:
    print(p)
