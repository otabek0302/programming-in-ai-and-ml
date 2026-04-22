# =============================================================
# PYTHON CASTING
# =============================================================

# Casting = forcing a specific data type onto a variable.
# Python is object-oriented, so it uses constructor functions to cast.

# int()   – from integer literal, float (drops decimals), or numeric string
# float() – from integer, float, or numeric string
# str()   – from almost any data type

# --- int() ---
x = int(1)    # 1
y = int(2.8)  # 2   (decimals are removed, NOT rounded)
z = int("3")  # 3   (string must represent a whole number)
print(x, y, z)

# --- float() ---
x = float(1)     # 1.0
y = float(2.8)   # 2.8
z = float("3")   # 3.0
w = float("4.2") # 4.2
print(x, y, z, w)

# --- str() ---
x = str("s1")  # 's1'
y = str(2)     # '2'
z = str(3.0)   # '3.0'
print(x, y, z)
print(type(x), type(y), type(z))

# --- Practical casting examples ---
user_input = "42"          # always a string from input()
number = int(user_input)   # convert before math
print(number + 8)          # 50

price = "9.99"
print(float(price) * 2)    # 19.98

count = 7
print("Count is: " + str(count))  # combine string + number safely
