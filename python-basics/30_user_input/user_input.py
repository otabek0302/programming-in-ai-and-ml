# =============================================================
# PYTHON USER INPUT
# =============================================================

# input() reads a line of text from the user and returns it as a STRING.
# Syntax:  variable = input(prompt)
# The program PAUSES until the user presses Enter.

# NOTE: The examples below use simulated input via mock/demo functions
# so this file can be run without interactive prompts.
# In real programs replace the demo calls with actual input() calls.

# =============================================================
# BASIC input()
# =============================================================

# Real usage (interactive):
# name = input("What is your name? ")
# print("Hello,", name)

# Demonstration (non-interactive):
def demo_basic():
    name = "Alice"           # simulates: name = input("What is your name? ")
    print(f"Hello, {name}!")

demo_basic()

# =============================================================
# INPUT ALWAYS RETURNS A STRING
# =============================================================

# Real:
# age = input("Enter your age: ")
# print(type(age))   # <class 'str'>  – even if user typed a number

# You must cast it to use it as a number:
# age = int(input("Enter your age: "))

def demo_types():
    age_str = "25"            # simulates input()
    age_int = int(age_str)
    print(type(age_str))      # <class 'str'>
    print(type(age_int))      # <class 'int'>
    print(f"In 10 years you will be {age_int + 10}")

demo_types()

# =============================================================
# CASTING INPUT
# =============================================================

# int()   – whole numbers
# float() – decimal numbers
# bool()  – True/False (careful: bool("False") is True!)

# Real:
# x = float(input("Enter a number: "))
# print(x * 2)

# =============================================================
# VALIDATING USER INPUT (guard against bad values)
# =============================================================

def get_positive_int(prompt, simulated_inputs):
    """Keep asking until a valid positive integer is entered."""
    i = 0
    while True:
        raw = simulated_inputs[i] if i < len(simulated_inputs) else "1"
        i += 1
        print(f"{prompt}{raw}")    # show what "user typed"
        try:
            value = int(raw)
            if value > 0:
                return value
            print("  Please enter a positive number.")
        except ValueError:
            print("  That's not a valid integer. Try again.")

result = get_positive_int("Enter a positive integer: ", ["abc", "-5", "0", "7"])
print(f"Got: {result}")   # 7

# =============================================================
# COMMON INPUT PATTERNS
# =============================================================

# --- Yes / No confirmation ---
def ask_yes_no(prompt, simulated="y"):
    print(f"{prompt} (y/n): {simulated}")
    return simulated.strip().lower() in ("y", "yes")

if ask_yes_no("Do you want to continue?", "yes"):
    print("Continuing...")
else:
    print("Stopping.")

# --- Choose from a menu ---
def choose_from_menu(options, simulated="2"):
    print("\nMenu:")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print(f"Your choice: {simulated}")
    try:
        choice = int(simulated)
        if 1 <= choice <= len(options):
            return options[choice - 1]
    except ValueError:
        pass
    return None

menu = ["View profile", "Edit settings", "Log out"]
selected = choose_from_menu(menu, "2")
print(f"Selected: {selected}")   # Edit settings

# --- Read multiple values on one line ---
def demo_multi():
    raw = "10 20 30"           # simulates: raw = input("Enter 3 numbers: ")
    numbers = list(map(int, raw.split()))
    print(numbers)             # [10, 20, 30]
    print(sum(numbers))        # 60

demo_multi()

# --- Read a list of comma-separated values ---
def demo_csv():
    raw = "apple, banana, cherry"   # simulates input()
    items = [x.strip() for x in raw.split(",")]
    print(items)    # ['apple', 'banana', 'cherry']

demo_csv()

# =============================================================
# getpass  – hidden input for passwords
# =============================================================

# getpass.getpass() works like input() but does NOT echo characters.
# Use this for passwords, PINs, API keys.

import getpass

# Real usage:
# password = getpass.getpass("Enter password: ")

# Note: in non-interactive scripts/notebooks it falls back to input()
# and may show a warning. That's fine for demo purposes.

# =============================================================
# sys.stdin  – reading input programmatically
# =============================================================

import sys

# Read all lines from stdin (useful in scripts / piped input)
# for line in sys.stdin:
#     print(line.strip())

# Read one line
# line = sys.stdin.readline().strip()

# =============================================================
# REAL-WORLD TEMPLATE  (copy this pattern for interactive programs)
# =============================================================

def run_calculator():
    """Simple command-line calculator template."""
    # In real code replace the simulated values with actual input() calls.
    pairs = [("10", "5", "+"), ("9", "3", "/"), ("4", "0", "/")]

    for a_str, b_str, op in pairs:
        print(f"\nEnter first number:  {a_str}")
        print(f"Enter second number: {b_str}")
        print(f"Enter operator (+, -, *, /): {op}")

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid number.")
            continue

        match op:
            case "+": print(f"Result: {a + b}")
            case "-": print(f"Result: {a - b}")
            case "*": print(f"Result: {a * b}")
            case "/":
                if b == 0:
                    print("Error: division by zero")
                else:
                    print(f"Result: {a / b}")
            case _:
                print("Unknown operator")

run_calculator()
