# =============================================================
# PYTHON TRY...EXCEPT
# =============================================================

# Error handling lets a program respond to errors gracefully
# instead of crashing.
# Syntax:
#   try:       – code that might raise an exception
#   except:    – code that runs if an exception occurs
#   else:      – code that runs if NO exception occurred
#   finally:   – code that ALWAYS runs (cleanup)

# =============================================================
# BASIC TRY...EXCEPT
# =============================================================

try:
    print(1 / 0)
except:
    print("An error occurred!")   # catches any exception

# =============================================================
# CATCHING A SPECIFIC EXCEPTION
# =============================================================

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# =============================================================
# MULTIPLE EXCEPT BLOCKS
# =============================================================

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: division by zero")
    except TypeError:
        print("Error: invalid types – numbers required")

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Error: division by zero
print(safe_divide(10, "x"))   # Error: invalid types

# =============================================================
# CATCH MULTIPLE EXCEPTIONS IN ONE LINE
# =============================================================

def parse(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        print(f"Cannot convert {value!r} to int")
        return None

print(parse("42"))     # 42
print(parse("abc"))    # Cannot convert 'abc' to int
print(parse(None))     # Cannot convert None to int

# =============================================================
# ACCESS THE EXCEPTION OBJECT WITH "as"
# =============================================================

try:
    x = int("not a number")
except ValueError as e:
    print(f"ValueError caught: {e}")
    print(f"Type: {type(e).__name__}")

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

# =============================================================
# ELSE  – runs only when NO exception occurred
# =============================================================

def safe_open(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    else:
        print(f"File opened: {f.read()[:50]}")
        f.close()

safe_open("nonexistent.txt")

# =============================================================
# FINALLY  – ALWAYS runs (use for cleanup)
# =============================================================

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        result = None
    finally:
        print("finally block always runs")
    return result

print(divide(10, 2))   # runs + returns 5.0
print(divide(10, 0))   # exception + finally + returns None

# =============================================================
# RAISE  – deliberately trigger an exception
# =============================================================

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range (0-150)")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    set_age("thirty")
except TypeError as e:
    print(f"TypeError: {e}")

# re-raise an exception after logging
def process(data):
    try:
        return int(data)
    except ValueError as e:
        print(f"Logging error: {e}")
        raise    # re-raises the same exception

try:
    process("bad")
except ValueError:
    print("Handled at the top level")

# =============================================================
# CUSTOM EXCEPTIONS
# =============================================================

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount} – balance is only {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
    print(f"  balance: {e.balance}, requested: {e.amount}")

# =============================================================
# COMMON BUILT-IN EXCEPTIONS
# =============================================================

exceptions = [
    ("SyntaxError",       "Invalid Python syntax"),
    ("NameError",         "Variable not found"),
    ("TypeError",         "Wrong type for operation"),
    ("ValueError",        "Right type, wrong value"),
    ("IndexError",        "List index out of range"),
    ("KeyError",          "Dict key not found"),
    ("AttributeError",    "Object has no such attribute"),
    ("ZeroDivisionError", "Division or modulo by zero"),
    ("FileNotFoundError", "File doesn't exist"),
    ("ImportError",       "Module not found"),
    ("RuntimeError",      "Detected during execution"),
    ("StopIteration",     "Iterator has no more items"),
    ("OverflowError",     "Arithmetic result too large"),
    ("MemoryError",       "Out of memory"),
    ("RecursionError",    "Maximum recursion depth exceeded"),
    ("OSError",           "Operating system error (parent of FileNotFoundError)"),
    ("Exception",         "Base class for all non-system-exit exceptions"),
    ("BaseException",     "Base class for ALL exceptions including SystemExit"),
]

for name, desc in exceptions:
    print(f"  {name:<22} – {desc}")

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Safe integer conversion ---
def to_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(to_int("42"))       # 42
print(to_int("abc"))      # 0
print(to_int(None, -1))   # -1

# --- Retry pattern ---
def fetch_data(attempt):
    if attempt < 3:
        raise ConnectionError("Network unavailable")
    return "data received"

for i in range(1, 5):
    try:
        result = fetch_data(i)
        print(f"Success on attempt {i}: {result}")
        break
    except ConnectionError as e:
        print(f"Attempt {i} failed: {e}")

# --- Context manager (with statement) for safe file handling ---
try:
    with open("test.txt", "w") as f:
        f.write("hello")
    with open("test.txt", "r") as f:
        print(f.read())    # hello
except IOError as e:
    print(f"File error: {e}")
finally:
    import os
    if os.path.exists("test.txt"):
        os.remove("test.txt")
