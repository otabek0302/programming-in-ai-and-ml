# =============================================================
# PYTHON BOOLEANS
# =============================================================

# Booleans represent one of two values: True or False.
# Used in conditions, comparisons, and control flow.

print(True)
print(False)

# =============================================================
# BOOLEAN FROM COMPARISONS
# =============================================================

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

x = 10
y = 9
print(x > y)    # True  – used directly in conditions

if x > y:
    print("x is greater than y")

# =============================================================
# bool() – EVALUATE ANY VALUE AS BOOLEAN
# =============================================================

# Most values are True by default.
# The following are False:
#   - Empty values: "", (), [], {}, set()
#   - Zero:         0, 0.0, 0j
#   - None
#   - False itself
#   - Objects with __bool__() returning False

print(bool("Hello"))    # True  – non-empty string
print(bool(15))         # True  – non-zero number
print(bool(["a", "b"])) # True  – non-empty list

print(bool(""))         # False – empty string
print(bool(0))          # False – zero
print(bool([]))         # False – empty list
print(bool(()))         # False – empty tuple
print(bool({}))         # False – empty dict
print(bool(None))       # False

# =============================================================
# FUNCTIONS RETURNING BOOLEANS
# =============================================================

# isinstance() checks if an object is of a certain type.
print(isinstance(10, int))    # True
print(isinstance("hi", str))  # True
print(isinstance(3.14, int))  # False

# =============================================================
# BOOLEANS ARE INTEGERS UNDER THE HOOD
# =============================================================

# True == 1, False == 0
print(True + True)   # 2
print(True + False)  # 1
print(False + False) # 0
print(True * 5)      # 5
print(int(True))     # 1
print(int(False))    # 0
