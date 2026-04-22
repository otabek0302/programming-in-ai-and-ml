# =============================================================
# PYTHON MATCH STATEMENT  (Python 3.10+)
# =============================================================

# match is Python's structural pattern matching.
# Similar to switch/case in other languages, but far more powerful.
# Syntax:
#   match subject:
#       case pattern:
#           ...

import sys
print(f"Python version: {sys.version}")

# =============================================================
# BASIC MATCH  (like switch/case)
# =============================================================

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:           # default / wildcard
            return "Unknown status"

print(http_status(200))   # OK
print(http_status(404))   # Not Found
print(http_status(999))   # Unknown status

# =============================================================
# MATCHING STRINGS
# =============================================================

def greet(language):
    match language:
        case "english":
            return "Hello!"
        case "spanish":
            return "¡Hola!"
        case "french":
            return "Bonjour!"
        case "uzbek":
            return "Salom!"
        case _:
            return f"Hello! (language '{language}' not supported)"

print(greet("english"))   # Hello!
print(greet("uzbek"))     # Salom!
print(greet("german"))    # Hello! (language 'german' not supported)

# =============================================================
# OR PATTERNS  (combine multiple cases with |)
# =============================================================

def day_type(day):
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Unknown"

print(day_type("Saturday"))   # Weekend
print(day_type("Monday"))     # Weekday

# =============================================================
# MATCHING TUPLES / SEQUENCES
# =============================================================

def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On x-axis at x={x}"
        case (0, y):
            return f"On y-axis at y={y}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(describe_point((0, 0)))    # Origin
print(describe_point((5, 0)))    # On x-axis at x=5
print(describe_point((0, 3)))    # On y-axis at y=3
print(describe_point((4, 7)))    # Point at (4, 7)

# =============================================================
# MATCHING DICTIONARIES
# =============================================================

def process_command(command):
    match command:
        case {"action": "quit"}:
            return "Quitting..."
        case {"action": "go", "direction": direction}:
            return f"Going {direction}"
        case {"action": "get", "item": item}:
            return f"Getting {item}"
        case _:
            return "Unknown command"

print(process_command({"action": "quit"}))
print(process_command({"action": "go", "direction": "north"}))
print(process_command({"action": "get", "item": "sword"}))
print(process_command({"action": "fly"}))

# =============================================================
# GUARDS  (add extra condition with if)
# =============================================================

def classify_number(n):
    match n:
        case x if x < 0:
            return f"{x} is negative"
        case 0:
            return "zero"
        case x if x % 2 == 0:
            return f"{x} is positive and even"
        case x:
            return f"{x} is positive and odd"

print(classify_number(-5))   # -5 is negative
print(classify_number(0))    # zero
print(classify_number(4))    # 4 is positive and even
print(classify_number(7))    # 7 is positive and odd

# =============================================================
# MATCHING CLASS INSTANCES
# =============================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, radius):
        self.radius = radius

def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "Point at origin"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case Circle(radius=r) if r > 0:
            return f"Circle with radius {r}"
        case _:
            return "Unknown shape"

print(describe_shape(Point(0, 0)))    # Point at origin
print(describe_shape(Point(3, 4)))    # Point at (3, 4)
print(describe_shape(Circle(5)))      # Circle with radius 5

# =============================================================
# CAPTURING WITH AS
# =============================================================

def handle(event):
    match event:
        case {"type": "click", "position": (x, y) as pos}:
            return f"Click at {pos} → x={x}, y={y}"
        case {"type": "keypress", "key": key}:
            return f"Key pressed: {key}"
        case _:
            return "Unhandled event"

print(handle({"type": "click", "position": (100, 200)}))
print(handle({"type": "keypress", "key": "Enter"}))
