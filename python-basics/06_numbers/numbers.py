# =============================================================
# PYTHON NUMBERS
# =============================================================

# Three numeric types in Python:
# int     – whole numbers, positive or negative, no decimals, unlimited length
# float   – numbers with a decimal point
# complex – written with a "j" as imaginary part

x = 1      # int
y = 2.8    # float
z = 1j     # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# --- Int examples ---
x = 1
y = 35656222554887711
z = -3255522
print(type(x), type(y), type(z))

# --- Float examples ---
x = 1.10
y = 1.0
z = -35.59
print(type(x), type(y), type(z))

# Floats can also be scientific notation (e = power of 10).
x = 35e3    # 35000.0
y = 12E4    # 120000.0
z = -87.7e100
print(type(x), type(y), type(z))

# --- Complex examples ---
x = 3+5j
y = 5j
z = -5j
print(type(x), type(y), type(z))

# --- Type conversion between numerics ---
x = 1       # int
y = 2.8     # float
z = 1j      # complex

a = float(x)    # int → float
b = int(y)      # float → int  (truncates decimals)
c = complex(x)  # int → complex

print(a)        # 1.0
print(b)        # 2
print(c)        # (1+0j)

# Note: you cannot convert a complex number to int or float.
# int(1j)  → TypeError

# --- Random numbers ---
# Python has no built-in random() function, but has a random module.
import random
print(random.randrange(1, 10))  # random int between 1 and 9
