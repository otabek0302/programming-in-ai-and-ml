# =============================================================
# PYTHON VARIABLES
# =============================================================

# Variables are containers for storing data values.
# No declaration command needed – a variable is created on first assignment.

x = 5
y = "John"
print(x)
print(y)

# Variables can change type after being set (dynamic typing).
x = 4        # int
x = "Sally"  # now str
print(x)

# --- Casting (force a specific type) ---
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0

# --- Get the type ---
x = 5
y = "John"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# --- Single vs double quotes – same result ---
x = "John"
x = 'John'

# --- Case-sensitive ---
a = 4
A = "Sally"  # A and a are different variables

# =============================================================
# VARIABLE NAMING RULES
# =============================================================
# Must start with a letter or underscore (_)
# Cannot start with a number
# Can only contain letters, numbers, and underscores (A-z, 0-9, _)
# Case-sensitive
# Cannot be a Python keyword (if, for, while, etc.)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# ILLEGAL names (would cause SyntaxError):
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# --- Naming styles ---
myVariableName = "John"   # camelCase
MyVariableName = "John"   # PascalCase
my_variable_name = "John" # snake_case  ← Python convention

# =============================================================
# ASSIGNING VALUES
# =============================================================

# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# =============================================================
# OUTPUT VARIABLES
# =============================================================

x = "Python is awesome"
print(x)

# Multiple variables with comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Multiple strings with + (manual spaces needed)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Note: + between string and number raises TypeError.
# print("Age: " + 25)  # ERROR – use comma instead
print("Age:", 25)       # works

# =============================================================
# GLOBAL VARIABLES
# =============================================================

x = "awesome"

def myfunc():
    print("Python is " + x)  # reads the global x

myfunc()

# Local variable shadows the global inside the function.
x = "awesome"

def myfunc():
    x = "fantastic"          # local only
    print("Python is " + x)

myfunc()
print("Python is " + x)     # still "awesome"

# --- global keyword: create/modify a global inside a function ---
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)     # "fantastic"
