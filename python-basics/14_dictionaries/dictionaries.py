# =============================================================
# PYTHON DICTIONARIES
# =============================================================

# Dictionaries store data as key:value pairs.
# Properties:
#   - Ordered*       (insertion order is preserved, Python 3.7+)
#   - Changeable     (can add, remove, or update items)
#   - No duplicate keys (a duplicate key overwrites the old value)
# * Prior to Python 3.7 dictionaries were unordered.

person = {"name": "John", "age": 36, "city": "New York"}
print(person)
print(len(person))   # 3

# Values can be any data type; keys must be immutable (str, int, tuple)
mixed = {
    "name": "Alice",
    "scores": [95, 87, 92],
    "active": True,
    "address": {"city": "Oslo", "country": "Norway"},
}

# Duplicate key – last value wins
d = {"brand": "Ford", "model": "Mustang", "brand": "Tesla"}
print(d)   # {"brand": "Tesla", "model": "Mustang"}

# dict() constructor
car = dict(brand="Ford", model="Mustang", year=1964)
print(car)

# =============================================================
# ACCESSING ITEMS
# =============================================================

person = {"name": "John", "age": 36, "city": "New York"}

print(person["name"])          # John   – bracket notation (KeyError if missing)
print(person.get("name"))      # John   – .get() returns None if key missing
print(person.get("email"))     # None
print(person.get("email", "not found"))  # custom default value

# keys(), values(), items()
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['John', 36, 'New York'])
print(person.items())   # dict_items([('name', 'John'), ('age', 36), ...])

# These views update automatically when the dict changes
keys_view = person.keys()
person["email"] = "john@example.com"
print(keys_view)   # dict_keys(['name', 'age', 'city', 'email'])

# Check if a key exists
if "name" in person:
    print("name key exists")

# =============================================================
# CHANGING / ADDING ITEMS
# =============================================================

person = {"name": "John", "age": 36}

person["age"] = 40              # update existing key
person["email"] = "john@x.com" # add new key
print(person)

person.update({"age": 45, "city": "Boston"})  # update multiple at once
print(person)

# =============================================================
# REMOVING ITEMS
# =============================================================

person = {"name": "John", "age": 36, "city": "New York", "email": "j@x.com"}

removed = person.pop("email")      # remove by key, returns value
print(removed)                     # j@x.com
print(person)

last = person.popitem()            # remove and return the LAST inserted item
print(last)                        # ('city', 'New York')
print(person)

del person["age"]                  # delete by key
print(person)

del person                         # delete the entire dict variable
# print(person)                    # NameError

person = {"name": "John", "age": 36}
person.clear()                     # empty the dict; variable still exists
print(person)                      # {}

# =============================================================
# LOOPING THROUGH A DICTIONARY
# =============================================================

person = {"name": "John", "age": 36, "city": "New York"}

# Loop over keys (default)
for key in person:
    print(key)

# Loop over keys explicitly
for key in person.keys():
    print(key)

# Loop over values
for value in person.values():
    print(value)

# Loop over key:value pairs
for key, value in person.items():
    print(key, "->", value)

# =============================================================
# COPYING A DICTIONARY
# =============================================================

original = {"name": "John", "age": 36}

# WRONG: creates another reference to the same dict
ref = original
ref["age"] = 99
print(original)   # {"name": "John", "age": 99}  – original changed!

# CORRECT – copy()
original = {"name": "John", "age": 36}
copy1 = original.copy()
copy1["age"] = 99
print(original)   # {"name": "John", "age": 36}  – safe

# CORRECT – dict() constructor
copy2 = dict(original)

# Note: both copy() and dict() are SHALLOW copies.
# Nested objects (lists, dicts) are still shared.
# Use copy.deepcopy() for a fully independent copy.
import copy
nested = {"name": "John", "scores": [95, 87]}
deep = copy.deepcopy(nested)
deep["scores"].append(100)
print(nested)    # {"name": "John", "scores": [95, 87]}  – unchanged

# =============================================================
# NESTED DICTIONARIES
# =============================================================

family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

print(family["child1"]["name"])   # Emil
print(family["child3"]["year"])   # 2011

# Loop nested dict
for person_key, person_info in family.items():
    print(f"\n{person_key}:")
    for key, value in person_info.items():
        print(f"  {key}: {value}")

# =============================================================
# DICTIONARY COMPREHENSION
# =============================================================

# Syntax: {key: value for item in iterable if condition}

squares = {x: x ** 2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter: only even squares
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# =============================================================
# USEFUL PATTERNS
# =============================================================

# setdefault() – return value if key exists; insert default if not
counts = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# Merge two dicts (Python 3.9+ supports | operator)
defaults = {"theme": "dark", "lang": "en", "timeout": 30}
user_prefs = {"lang": "uz", "timeout": 60}
config = defaults | user_prefs          # user_prefs values win on collision
print(config)   # {'theme': 'dark', 'lang': 'uz', 'timeout': 60}

# Older approach (works in all Python 3 versions)
config = {**defaults, **user_prefs}
print(config)

# =============================================================
# DICTIONARY METHODS – QUICK REFERENCE
# =============================================================

# clear()               – remove all items
# copy()                – return a shallow copy
# fromkeys(keys, val)   – create dict from a list of keys with same value
# get(key, default)     – return value or default if key missing
# items()               – return view of (key, value) pairs
# keys()                – return view of all keys
# values()              – return view of all values
# pop(key, default)     – remove and return value for key
# popitem()             – remove and return last (key, value) pair
# setdefault(key, val)  – return value; insert key with val if not present
# update(dict)          – update dict with pairs from another dict/iterable

template = dict.fromkeys(["name", "age", "city"], "unknown")
print(template)   # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
