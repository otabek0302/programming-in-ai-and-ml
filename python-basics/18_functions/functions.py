# =============================================================
# PYTHON FUNCTIONS
# =============================================================

# A function is a reusable block of code that runs when called.
# Defined with the def keyword.
# Syntax:
#   def function_name(parameters):
#       ...

# =============================================================
# BASIC FUNCTION
# =============================================================

def greet():
    print("Hello from a function!")

greet()   # call the function

# =============================================================
# PARAMETERS & ARGUMENTS
# =============================================================

# Parameter = the variable in the definition
# Argument  = the value you pass when calling

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# --- Multiple parameters ---
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hi")
greet("Bob", "Good morning")

# =============================================================
# DEFAULT PARAMETER VALUES
# =============================================================

# If an argument is not passed, the default is used.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hey")         # Hey, Bob!

# =============================================================
# KEYWORD ARGUMENTS (order doesn't matter)
# =============================================================

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="dog", name="Rex")
describe_pet(name="Whiskers", animal="cat")   # reversed order – still works

# =============================================================
# *args – arbitrary number of positional arguments
# =============================================================

# Stored as a tuple inside the function.
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(1, 2, 3))         # 6
print(add(10, 20, 30, 40))  # 100

def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")

# =============================================================
# **kwargs – arbitrary number of keyword arguments
# =============================================================

# Stored as a dict inside the function.
def print_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="Oslo")

# =============================================================
# COMBINING *args AND **kwargs
# =============================================================

# Order: regular → *args → default → **kwargs
def mixed(name, *hobbies, greeting="Hello", **extra):
    print(f"{greeting}, {name}!")
    print("Hobbies:", hobbies)
    print("Extra:", extra)

mixed("Alice", "reading", "cycling", greeting="Hi", country="Norway")

# =============================================================
# RETURN VALUES
# =============================================================

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)   # 20

# Return multiple values (returned as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 5, 2])
print(low, high)   # 1 9

# Early return
def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(4))   # True
print(is_even(7))   # False

# A function with no return statement returns None implicitly.
def say_hi():
    print("Hi!")

result = say_hi()
print(result)   # None

# =============================================================
# PASS – empty function body placeholder
# =============================================================

def my_function():
    pass    # valid; avoids IndentationError while planning

# =============================================================
# VARIABLE SCOPE
# =============================================================

# local variable – exists only inside the function
def demo():
    x = 10          # local
    print(x)

demo()
# print(x)   # NameError – x doesn't exist outside

# global variable – accessible everywhere
x = "global"

def demo():
    print(x)        # reads global x

demo()
print(x)

# global keyword – modify a global variable inside a function
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)   # 2

# =============================================================
# RECURSION
# =============================================================

# A function that calls itself.
# Must have a base case to avoid infinite recursion.

def factorial(n):
    if n == 0:        # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)
print(factorial(0))   # 1

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13
print()

# =============================================================
# DOCSTRINGS
# =============================================================

# A string literal on the first line of a function becomes its docstring.
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add.__doc__)   # Return the sum of a and b.
help(add)            # formatted docstring in terminal

# =============================================================
# TYPE HINTS  (Python 3.5+)
# =============================================================

# Hints do not enforce types at runtime but improve readability and IDE support.
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

print(greet("Alice"))
print(add(3, 4))

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Temperature converter ---
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

print(celsius_to_fahrenheit(100))   # 212.0
print(fahrenheit_to_celsius(212))   # 100.0

# --- FizzBuzz as a function ---
def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)

for i in range(1, 16):
    print(fizzbuzz(i), end=" ")
print()

# --- Grader ---
def get_grade(score: int) -> str:
    if score >= 90:   return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"

for s in [95, 83, 74, 61, 45]:
    print(f"{s} → {get_grade(s)}")
