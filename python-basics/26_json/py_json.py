# =============================================================
# PYTHON JSON
# =============================================================

# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# Python has a built-in json module to encode/decode JSON.
#
# Conversion table:
#   Python → JSON          JSON → Python
#   dict   → object        object  → dict
#   list   → array         array   → list
#   tuple  → array         -       → -
#   str    → string        string  → str
#   int    → number        number  → int or float
#   float  → number
#   True   → true          true    → True
#   False  → false         false   → False
#   None   → null          null    → None

import json

# =============================================================
# json.dumps()  – Python object → JSON string  (encode / serialize)
# =============================================================

# dict → JSON string
person = {"name": "Alice", "age": 30, "city": "Oslo"}
json_str = json.dumps(person)
print(json_str)           # {"name": "Alice", "age": 30, "city": "Oslo"}
print(type(json_str))     # <class 'str'>

# Pretty-print with indentation
print(json.dumps(person, indent=4))

# All Python types
data = {
    "name": "Bob",
    "age": 25,
    "height": 1.80,
    "active": True,
    "nickname": None,
    "scores": [95, 87, 92],
    "address": {"city": "Paris", "zip": "75001"},
}
print(json.dumps(data, indent=2))

# Sort keys alphabetically
print(json.dumps(person, indent=4, sort_keys=True))

# Separators – compact JSON (no spaces)
print(json.dumps(person, separators=(",", ":")))
# {"name":"Alice","age":30,"city":"Oslo"}

# =============================================================
# json.loads()  – JSON string → Python object  (decode / deserialize)
# =============================================================

json_string = '{"name": "Alice", "age": 30, "active": true, "score": null}'
obj = json.loads(json_string)
print(obj)             # {'name': 'Alice', 'age': 30, 'active': True, 'score': None}
print(type(obj))       # <class 'dict'>
print(obj["name"])     # Alice
print(obj["active"])   # True  (JSON true → Python True)
print(obj["score"])    # None  (JSON null → Python None)

# JSON array → Python list
json_array = '[1, 2, 3, "hello", true, null]'
result = json.loads(json_array)
print(result)          # [1, 2, 3, 'hello', True, None]
print(type(result))    # <class 'list'>

# Nested JSON
nested_json = '''
{
    "users": [
        {"id": 1, "name": "Alice", "admin": true},
        {"id": 2, "name": "Bob",   "admin": false}
    ]
}
'''
data = json.loads(nested_json)
for user in data["users"]:
    print(f"  {user['name']} – admin: {user['admin']}")

# =============================================================
# json.dump()  – Python object → JSON FILE  (write to file)
# =============================================================

person = {"name": "Alice", "age": 30, "city": "Oslo"}

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

print("Written to person.json")

# =============================================================
# json.load()  – JSON FILE → Python object  (read from file)
# =============================================================

with open("person.json", "r") as f:
    loaded = json.load(f)

print(loaded)                 # {'name': 'Alice', 'age': 30, 'city': 'Oslo'}
print(loaded["name"])         # Alice

# =============================================================
# CUSTOM SERIALIZATION  (objects not natively JSON serializable)
# =============================================================

import datetime

# datetime is not JSON serializable by default
now = datetime.datetime.now()

# Option 1: convert manually before dumping
data = {"timestamp": now.isoformat(), "value": 42}
print(json.dumps(data))

# Option 2: custom encoder
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return super().default(obj)

event = {"name": "Launch", "date": datetime.datetime(2025, 6, 15, 9, 0)}
print(json.dumps(event, cls=DateTimeEncoder, indent=2))

# Option 3: default parameter (function called for unknown types)
def serialize(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

print(json.dumps(event, default=serialize, indent=2))

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Config file ---
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
    },
    "allowed_hosts": ["localhost", "127.0.0.1"],
}

# Save config
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

# Load config
with open("config.json", "r") as f:
    loaded_config = json.load(f)

print(loaded_config["app_name"])
print(loaded_config["database"]["host"])

# --- API response simulation ---
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob",   "email": "bob@example.com"}
        ],
        "total": 2
    }
}
'''

response = json.loads(api_response)
if response["status"] == "success":
    users = response["data"]["users"]
    for u in users:
        print(f"  ID {u['id']}: {u['name']} ({u['email']})")

# --- Deep copy via JSON (simple objects only) ---
original = {"a": [1, 2, 3], "b": {"x": 10}}
deep_copy = json.loads(json.dumps(original))
deep_copy["a"].append(99)
print(original)    # unchanged
print(deep_copy)   # has 99

# Clean up files
import os
for fname in ["person.json", "config.json"]:
    if os.path.exists(fname):
        os.remove(fname)
