# =============================================================
# PYTHON DATA TYPES
# =============================================================

# Python built-in data types:
# Text Type:      str
# Numeric Types:  int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:   dict
# Set Types:      set, frozenset
# Boolean Type:   bool
# Binary Types:   bytes, bytearray, memoryview
# None Type:      NoneType

# --- Get the data type ---
x = 5
print(type(x))  # <class 'int'>

# =============================================================
# SETTING THE DATA TYPE (automatic, based on assigned value)
# =============================================================

x = "Hello World"                               # str
x = 20                                          # int
x = 20.5                                        # float
x = 1j                                          # complex
x = ["apple", "banana", "cherry"]               # list
x = ("apple", "banana", "cherry")               # tuple
x = range(6)                                    # range
x = {"name": "John", "age": 36}                 # dict
x = {"apple", "banana", "cherry"}               # set
x = frozenset({"apple", "banana", "cherry"})    # frozenset
x = True                                        # bool
x = b"Hello"                                    # bytes
x = bytearray(5)                                # bytearray
x = memoryview(bytes(5))                        # memoryview
x = None                                        # NoneType

# =============================================================
# SETTING A SPECIFIC DATA TYPE (constructor functions)
# =============================================================

x = str("Hello World")                          # str
x = int(20)                                     # int
x = float(20.5)                                 # float
x = complex(1j)                                 # complex
x = list(("apple", "banana", "cherry"))         # list
x = tuple(("apple", "banana", "cherry"))        # tuple
x = range(6)                                    # range
x = dict(name="John", age=36)                   # dict
x = set(("apple", "banana", "cherry"))          # set
x = frozenset(("apple", "banana", "cherry"))    # frozenset
x = bool(5)                                     # bool
x = bytes(5)                                    # bytes
x = bytearray(5)                                # bytearray
x = memoryview(bytes(5))                        # memoryview

print(type(str("Hello World")))                 # <class 'str'>
print(type(int(20)))                            # <class 'int'>
print(type(float(20.5)))                        # <class 'float'>
print(type(list(("a", "b"))))                   # <class 'list'>
print(type(dict(name="John")))                  # <class 'dict'>
print(type(bool(5)))                            # <class 'bool'>
print(type(None))                               # <class 'NoneType'>

