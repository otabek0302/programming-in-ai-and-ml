# =============================================================
# PYTHON SYNTAX
# =============================================================

# Run directly in terminal:   python syntax.py
# Or in Command Line:         python myfile.py

# --- Indentation ---
# Python uses indentation to define blocks of code.
# Other languages use curly-brackets {}; Python uses spaces.

if 5 > 2:
    print("Five is greater than two!")  # 4 spaces (standard)

# The number of spaces must be consistent within the same block.
if 5 > 2:
    print("One space works too")       # 1 space – valid but uncommon

# WRONG: mixing indentation levels in the same block causes IndentationError
# if 5 > 2:
#  print("This line has 1 space")
#         print("This line has 8 spaces")  # ERROR!

# --- Statements ---
# A statement is one instruction. In Python, a statement ends at the end of the line.
# No semicolons needed (unlike Java or C).

print("Python is fun!")

# Multiple statements execute top-to-bottom, in order.
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

# --- Output ---
# print() displays text or values.
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")

# Strings must be inside quotes (single or double).
print("This will work!")
print('This will also work!')

# Numbers – no quotes needed.
print(10)
print(3 + 3)   # math inside print()
print(2 * 5)

# Mix text and numbers with a comma.
print("I am", 35, "years old.")
