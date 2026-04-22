# =============================================================
# PYTHON OPERATORS
# =============================================================

# Python operator groups:
# 1. Arithmetic
# 2. Assignment
# 3. Comparison
# 4. Logical
# 5. Identity
# 6. Membership
# 7. Bitwise

# =============================================================
# 1. ARITHMETIC OPERATORS
# =============================================================

x, y = 10, 3

print(x + y)    # 13  – Addition
print(x - y)    # 7   – Subtraction
print(x * y)    # 30  – Multiplication
print(x / y)    # 3.333... – Division (always returns float)
print(x // y)   # 3   – Floor division (drops decimals)
print(x % y)    # 1   – Modulus (remainder)
print(x ** y)   # 1000 – Exponentiation (10 to the power of 3)

# =============================================================
# 2. ASSIGNMENT OPERATORS
# =============================================================

x = 5       # assign
x += 3      # x = x + 3  → 8
x -= 2      # x = x - 2  → 6
x *= 4      # x = x * 4  → 24
x /= 3      # x = x / 3  → 8.0
x //= 2     # x = x // 2 → 4.0
x %= 3      # x = x % 3  → 1.0
x **= 4     # x = x ** 4 → 1.0

x = 10
x &= 5      # bitwise AND  → 0
x = 10
x |= 5      # bitwise OR   → 15
x = 10
x ^= 5      # bitwise XOR  → 15
x = 10
x >>= 1     # right shift  → 5
x = 10
x <<= 1     # left shift   → 20

# =============================================================
# 3. COMPARISON OPERATORS  (always return True or False)
# =============================================================

a, b = 5, 3

print(a == b)   # False – Equal
print(a != b)   # True  – Not equal
print(a > b)    # True  – Greater than
print(a < b)    # False – Less than
print(a >= b)   # True  – Greater than or equal to
print(a <= b)   # False – Less than or equal to

# =============================================================
# 4. LOGICAL OPERATORS
# =============================================================

x = 5

print(x > 3 and x < 10)    # True  – both conditions True
print(x > 3 and x > 10)    # False – second condition False

print(x > 3 or x > 10)     # True  – at least one True
print(x < 3 or x > 10)     # False – both False

print(not (x > 3))          # False – reverses True → False
print(not (x > 10))         # True  – reverses False → True

# =============================================================
# 5. IDENTITY OPERATORS
# =============================================================

# is     → True if both variables point to the SAME object in memory
# is not → True if they point to DIFFERENT objects

a = ["apple", "banana"]
b = ["apple", "banana"]
c = a

print(a is c)       # True  – c is the same object as a
print(a is b)       # False – b is a different object (same value, different identity)
print(a is not b)   # True

print(a == b)       # True  – equal in value (== checks value, not identity)

# =============================================================
# 6. MEMBERSHIP OPERATORS
# =============================================================

# in     → True if value is found in a sequence
# not in → True if value is NOT found in a sequence

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       # True
print("grape" in fruits)        # False
print("grape" not in fruits)    # True

sentence = "Python is great"
print("Python" in sentence)     # True
print("java" not in sentence)   # True

# =============================================================
# 7. BITWISE OPERATORS  (work on integers at the binary level)
# =============================================================

a, b = 6, 3   # 6 = 110, 3 = 011 in binary

print(a & b)   # 2   – AND:  110 & 011 = 010
print(a | b)   # 7   – OR:   110 | 011 = 111
print(a ^ b)   # 5   – XOR:  110 ^ 011 = 101
print(~a)      # -7  – NOT:  inverts all bits
print(a << 1)  # 12  – Left shift:  110 → 1100
print(a >> 1)  # 3   – Right shift: 110 → 011

# =============================================================
# OPERATOR PRECEDENCE (high → low)
# =============================================================

# ()            – Parentheses (highest)
# **            – Exponentiation
# +x, -x, ~x   – Unary plus/minus/bitwise NOT
# *, /, //, %   – Multiplication, division, floor div, modulus
# +, -          – Addition, subtraction
# <<, >>        – Bitwise shifts
# &             – Bitwise AND
# ^             – Bitwise XOR
# |             – Bitwise OR
# ==, !=, >, <, >=, <=, is, is not, in, not in  – Comparisons
# not           – Logical NOT
# and           – Logical AND
# or            – Logical OR (lowest)

print(2 + 3 * 4)        # 14  – * before +
print((2 + 3) * 4)      # 20  – () overrides precedence
print(2 ** 3 ** 2)      # 512 – ** is right-associative: 2 ** (3**2) = 2**9
