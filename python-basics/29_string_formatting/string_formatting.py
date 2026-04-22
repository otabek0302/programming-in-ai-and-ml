# =============================================================
# PYTHON STRING FORMATTING
# =============================================================

# Four ways to format strings in Python:
#   1. % operator          (old style, C-like)
#   2. str.format()        (Python 2.6+)
#   3. f-strings           (Python 3.6+)  ← preferred
#   4. Template strings    (string module)

name = "Alice"
age  = 30
pi   = 3.14159

# =============================================================
# 1. % OPERATOR  (old style)
# =============================================================

print("Hello, %s!" % name)                   # Hello, Alice!
print("I am %d years old." % age)            # I am 30 years old.
print("Pi is %.2f" % pi)                     # Pi is 3.14

# Multiple values – use a tuple
print("Name: %s, Age: %d" % (name, age))

# Common format codes:
# %s – string         %d – integer        %f – float
# %e – scientific     %g – shorter of f/e %r – repr()
# %x – hex lowercase  %X – hex uppercase  %o – octal
# %% – literal %

print("Hex: %x" % 255)         # ff
print("Hex: %X" % 255)         # FF
print("Sci: %e" % 12345.6789)  # 1.234568e+04

# =============================================================
# 2. str.format()
# =============================================================

print("Hello, {}!".format(name))
print("I am {} years old.".format(age))

# Positional arguments
print("{0} is {1} years old. {0} loves Python.".format(name, age))

# Keyword arguments
print("{name} is {age} years old.".format(name=name, age=age))

# Formatting numbers
print("{:.2f}".format(pi))         # 3.14
print("{:10.2f}".format(pi))       # '      3.14'  – width 10
print("{:010.2f}".format(pi))      # '0000003.14'  – zero-padded

# Alignment
print("{:<10}|".format("left"))    # 'left      |'
print("{:>10}|".format("right"))   # '     right|'
print("{:^10}|".format("center"))  # '  center  |'
print("{:-^10}|".format("hi"))     # '----hi----|'

# Thousands separator
print("{:,}".format(1000000))      # 1,000,000
print("{:,.2f}".format(9999.9))    # 9,999.90

# Binary, octal, hex
print("{:b}".format(10))           # 1010
print("{:o}".format(10))           # 12
print("{:x}".format(255))          # ff
print("{:#x}".format(255))         # 0xff  – with prefix

# =============================================================
# 3. F-STRINGS  (Python 3.6+)  ← preferred modern approach
# =============================================================

# Simply prefix the string with f or F and put expressions in {}
print(f"Hello, {name}!")
print(f"I am {age} years old.")
print(f"Pi is {pi:.2f}")

# Any expression works inside {}
x, y = 10, 3
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"{'hello'.upper()}")
print(f"{len(name)} characters in {name!r}")

# Alignment and padding
print(f"{'left':<10}|")       # 'left      |'
print(f"{'right':>10}|")      # '     right|'
print(f"{'center':^10}|")     # '  center  |'
print(f"{'hi':-^10}|")        # '----hi----|'

# Numbers
print(f"{pi:.4f}")             # 3.1416
print(f"{1000000:,}")          # 1,000,000
print(f"{0.0042:.2%}")         # 0.42%
print(f"{255:#010x}")          # 0x000000ff
print(f"{255:b}")              # 11111111
print(f"{1234567890:_}")       # 1_234_567_890  – underscore separator (3.10+)

# Debugging with = (prints variable name and value)
value = 42
print(f"{value=}")             # value=42  – great for debugging

# Multi-line f-string
person = {"name": "Bob", "age": 25}
info = (
    f"Name:  {person['name']}\n"
    f"Age:   {person['age']}\n"
    f"Adult: {person['age'] >= 18}"
)
print(info)

# Nested f-strings (Python 3.12+)
width = 10
print(f"{'hello':>{width}}")   # '     hello'

# =============================================================
# 4. TEMPLATE STRINGS  (string module)
# =============================================================

from string import Template

t = Template("Hello, $name! You are $age years old.")
print(t.substitute(name=name, age=age))

# safe_substitute – leaves missing placeholders as-is (no KeyError)
t = Template("Hello, $name! Your code is $code.")
print(t.safe_substitute(name="Alice"))   # Hello, Alice! Your code is $code.

# =============================================================
# FORMAT SPEC MINI-LANGUAGE – QUICK REFERENCE
# =============================================================

# [[fill]align][sign][#][0][width][grouping][.precision][type]
#
# fill      – any character used for padding
# align     – < (left)  > (right)  ^ (center)  = (sign before padding)
# sign      – + (always show sign)  - (only negative)  space
# #         – alternate form (0x, 0b, 0o prefixes)
# 0         – zero-pad numbers
# width     – minimum field width
# grouping  – , (comma)  _ (underscore)
# .prec     – decimal digits for float / max chars for string
# type:
#   s  – string       d  – decimal int    f  – fixed float
#   e  – scientific   g  – general float  %  – percentage
#   b  – binary       o  – octal          x/X – hex lower/upper
#   n  – locale number

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Receipt ---
items = [("Apple",  1.20, 3),
         ("Banana", 0.50, 6),
         ("Cherry", 2.80, 1)]

print(f"\n{'Item':<10} {'Price':>7} {'Qty':>5} {'Total':>8}")
print("-" * 34)
grand = 0
for item, price, qty in items:
    total = price * qty
    grand += total
    print(f"{item:<10} {price:>7.2f} {qty:>5} {total:>8.2f}")
print("-" * 34)
print(f"{'TOTAL':<10} {'':>7} {'':>5} {grand:>8.2f}")

# --- Progress bar ---
def progress_bar(done, total, width=20):
    pct = done / total
    filled = int(width * pct)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {pct:.0%} ({done}/{total})"

for i in range(0, 11, 2):
    print(progress_bar(i, 10))
