# =============================================================
# PYTHON METACLASSES
# =============================================================

# Everything in Python is an object – including classes.
# A metaclass is the "class of a class": it controls how classes are created.
#
# Class creation flow:
#   class Foo(Base, metaclass=Meta):  →  Meta("Foo", (Base,), namespace)
#
# Default metaclass for all classes is  type.

# =============================================================
# type() – the default metaclass
# =============================================================

# type(object)          → returns the type of an object
# type(name, bases, ns) → creates a new class dynamically

print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type(int))         # <class 'type'>   – int's metaclass is type
print(type(type))        # <class 'type'>   – type is its own metaclass

# Dynamically create a class with type()
Dog = type(
    "Dog",
    (object,),                # base classes tuple
    {                         # class namespace dict
        "species": "Canis lupus",
        "bark": lambda self: f"{self.name} says Woof!",
        "__init__": lambda self, name: setattr(self, "name", name),
        "__repr__": lambda self: f"Dog({self.name!r})",
    }
)

rex = Dog("Rex")
print(rex)            # Dog('Rex')
print(rex.bark())     # Rex says Woof!
print(Dog.species)    # Canis lupus

# =============================================================
# CUSTOM METACLASS
# =============================================================

class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""

    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, url: str = "localhost"):
        self.url = url
        print(f"  Creating connection to {url}")

    def query(self, sql: str) -> str:
        return f"Results: {sql}"


db1 = DatabaseConnection("db://prod")
db2 = DatabaseConnection("db://other")   # __init__ NOT called again

print(db1 is db2)   # True – same object
print(db1.url)      # db://prod

# =============================================================
# METACLASS __new__ AND __init__
# =============================================================

class LoggedMeta(type):
    """Logs class creation."""

    def __new__(mcs, name, bases, namespace):
        print(f"  Creating class: {name}")
        print(f"    Bases: {[b.__name__ for b in bases]}")
        print(f"    Methods: {[k for k in namespace if not k.startswith('_')]}")
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        print(f"  Initialised class: {name}")


class MyModel(metaclass=LoggedMeta):
    def save(self): ...
    def delete(self): ...

class ChildModel(MyModel):
    def validate(self): ...

# =============================================================
# METACLASS FOR VALIDATION
# =============================================================

class StrictMeta(type):
    """Enforces that all public methods have type annotations."""

    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith("_"):
                annotations = getattr(attr_value, "__annotations__", {})
                if "return" not in annotations:
                    raise TypeError(
                        f"Method '{name}.{attr_name}' must have a return type annotation"
                    )
        return super().__new__(mcs, name, bases, namespace)


class StrictAPI(metaclass=StrictMeta):
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

    def double(self, x: int) -> int:
        return x * 2

s = StrictAPI()
print(s.greet("Alice"))

try:
    class BadAPI(metaclass=StrictMeta):
        def missing_annotation(self):    # no return type → TypeError
            pass
except TypeError as e:
    print(e)

# =============================================================
# METACLASS FOR AUTO-REGISTRATION
# =============================================================

class PluginMeta(type):
    """Automatically registers all subclasses."""
    _registry: dict[str, type] = {}

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if bases:   # don't register the base class itself
            PluginMeta._registry[name.lower()] = cls

    @classmethod
    def get_plugin(mcs, name: str) -> type:
        return mcs._registry[name]


class BaseParser(metaclass=PluginMeta):
    def parse(self, data: str) -> dict: ...

class JsonParser(BaseParser):
    def parse(self, data: str) -> dict:
        import json
        return json.loads(data)

class CsvParser(BaseParser):
    def parse(self, data: str) -> dict:
        lines = data.strip().split("\n")
        headers = lines[0].split(",")
        return {"headers": headers, "rows": lines[1:]}

class XmlParser(BaseParser):
    def parse(self, data: str) -> dict:
        return {"raw": data}


print(PluginMeta._registry)

# Dynamically select a parser by name
parser_name = "jsonparser"
parser = PluginMeta.get_plugin(parser_name)()
result = parser.parse('{"key": "value"}')
print(result)

# =============================================================
# __init_subclass__  (simpler alternative to metaclass for hooks)
# =============================================================

class Base:
    """Use __init_subclass__ instead of a metaclass for many use cases."""

    _subclasses: list[type] = []

    def __init_subclass__(cls, required: bool = False, **kwargs):
        super().__init_subclass__(**kwargs)
        Base._subclasses.append(cls)
        cls._required = required
        print(f"  Registered subclass: {cls.__name__} (required={required})")


class Alpha(Base, required=True):
    pass

class Beta(Base):
    pass

class Gamma(Beta):    # sub-sub-class also triggers __init_subclass__
    pass

print(Base._subclasses)

# =============================================================
# __class_getitem__  (enable [] syntax on a class)
# =============================================================

class TypedList:
    def __class_getitem__(cls, item_type):
        name = f"TypedList[{item_type.__name__}]"
        return type(name, (cls,), {"_type": item_type})

    def __init__(self):
        self._data = []

    def append(self, value):
        if not isinstance(value, self.__class__._type):
            raise TypeError(f"Expected {self.__class__._type.__name__}")
        self._data.append(value)


IntList = TypedList[int]
il = IntList()
il.append(1)
il.append(2)
try:
    il.append("oops")
except TypeError as e:
    print(e)

# =============================================================
# METACLASS vs class decorator vs __init_subclass__
# =============================================================

print("""
Tool                  | When to use
----------------------|-------------------------------------------
metaclass             | Intercept class CREATION itself (__new__, __init__)
                      | Modify the class object at creation time
                      | Use when you need full control over class building
                      |
class decorator       | Add/modify behaviour AFTER class is created
                      | Simpler syntax, easier to understand
                      | Use for one-off class transformations
                      |
__init_subclass__     | React when a SUBCLASS is defined
                      | Cleaner than a metaclass for subclass hooks
                      | Use for registration, validation of subclasses
""")
