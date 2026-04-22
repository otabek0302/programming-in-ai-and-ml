# =============================================================
# PYTHON IF...ELSE
# =============================================================

# Python uses indentation to define the block of code to run.
# Syntax:
#   if condition:
#       ...
#   elif condition:
#       ...
#   else:
#       ...

# =============================================================
# BASIC IF
# =============================================================

a = 33
b = 200

if b > a:
    print("b is greater than a")

# Nothing happens if the condition is False and there is no else.
if a > b:
    print("a is greater than b")   # not printed

# =============================================================
# IF...ELSE
# =============================================================

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# =============================================================
# IF...ELIF...ELSE
# =============================================================

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")      # this runs
else:
    print("a is greater than b")

# Multiple elif branches
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")   # Score: 75, Grade: C

# =============================================================
# SHORT HAND (TERNARY OPERATOR)
# =============================================================

# One-line if
a = 10
b = 20
if a > b: print("a is greater")

# One-line if...else  (ternary / conditional expression)
x = "adult" if a >= 18 else "minor"
print(x)   # minor

# Ternary can be used inside print directly
a = 2
b = 330
print("A") if a > b else print("B")   # B

# Multiple conditions in ternary
print("A") if a > b else print("=") if a == b else print("B")   # B

# =============================================================
# LOGICAL OPERATORS IN CONDITIONS
# =============================================================

a = 200
b = 33
c = 500

# and – both conditions must be True
if a > b and c > a:
    print("Both conditions are True")

# or – at least one condition must be True
if a > b or a > c:
    print("At least one condition is True")

# not – reverses the result
if not a > b:
    print("a is NOT greater than b")    # not printed
else:
    print("a IS greater than b")        # this prints

# =============================================================
# NESTED IF
# =============================================================

x = 41

if x > 10:
    print("x is above 10")
    if x > 20:
        print("and also above 20")
        if x > 30:
            print("and also above 30")
            if x > 40:
                print("and also above 40")

# =============================================================
# PASS STATEMENT
# =============================================================

# if blocks cannot be empty. Use pass as a placeholder.
a = 33
b = 200

if b > a:
    pass    # TODO: handle this later

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# Check even / odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Membership check
fruits = ["apple", "banana", "cherry"]
item = "mango"
if item in fruits:
    print(f"{item} is in the list")
else:
    print(f"{item} is NOT in the list")

# None check
user = None
if user is None:
    print("No user logged in")
else:
    print(f"Hello, {user}")

# Range check
age = 25
if 18 <= age <= 65:
    print("Working age")
else:
    print("Outside working age")
