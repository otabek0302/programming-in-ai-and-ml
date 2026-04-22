# =============================================================
# PYTHON MATH
# =============================================================

# Python has built-in math operators AND a math module for advanced functions.
# For complex/scientific work use the math or cmath modules.

import math

# =============================================================
# BUILT-IN MATH FUNCTIONS  (no import needed)
# =============================================================

print(abs(-7.5))          # 7.5   – absolute value
print(abs(-5))            # 5

print(round(3.14159, 2))  # 3.14  – round to 2 decimal places
print(round(3.5))         # 4     – rounds to nearest even (banker's rounding)
print(round(2.5))         # 2

print(min(3, 1, 4, 1, 5)) # 1    – smallest value
print(max(3, 1, 4, 1, 5)) # 5    – largest value
print(min([10, 20, 5]))   # 5    – also works on iterables
print(max([10, 20, 5]))   # 20

print(sum([1, 2, 3, 4]))  # 10   – sum of iterable
print(sum(range(1, 101))) # 5050

print(pow(2, 10))         # 1024  – 2 to the power of 10
print(pow(2, 10, 100))    # 24    – (2**10) % 100  (modular exponentiation)

print(divmod(17, 5))      # (3, 2) – (quotient, remainder)

# =============================================================
# math MODULE – CONSTANTS
# =============================================================

print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045  – Euler's number
print(math.tau)     # 6.283185307179586  – 2 * pi
print(math.inf)     # inf  – positive infinity
print(math.nan)     # nan  – Not a Number

print(-math.inf)            # -inf
print(math.isinf(math.inf)) # True
print(math.isnan(math.nan)) # True
print(math.isfinite(42))    # True
print(math.isfinite(math.inf)) # False

# =============================================================
# ROUNDING FUNCTIONS
# =============================================================

print(math.floor(3.9))    # 3   – round DOWN to nearest integer
print(math.floor(-3.1))   # -4

print(math.ceil(3.1))     # 4   – round UP to nearest integer
print(math.ceil(-3.9))    # -3

print(math.trunc(3.9))    # 3   – truncate decimal part (toward zero)
print(math.trunc(-3.9))   # -3

# =============================================================
# POWER & LOGARITHMS
# =============================================================

print(math.sqrt(16))       # 4.0   – square root
print(math.sqrt(2))        # 1.4142135623730951

print(math.pow(2, 8))      # 256.0 – always returns float (unlike built-in pow)
print(math.exp(1))         # 2.718...  – e^1
print(math.exp(2))         # 7.389...  – e^2

print(math.log(math.e))    # 1.0   – natural log (base e)
print(math.log(100, 10))   # 2.0   – log base 10
print(math.log2(8))        # 3.0   – log base 2
print(math.log10(1000))    # 3.0   – log base 10

# =============================================================
# TRIGONOMETRY  (angles in RADIANS)
# =============================================================

print(math.sin(0))                  # 0.0
print(math.cos(0))                  # 1.0
print(math.tan(0))                  # 0.0
print(math.sin(math.pi / 2))        # 1.0
print(math.cos(math.pi))            # -1.0

# Convert between degrees and radians
print(math.degrees(math.pi))        # 180.0
print(math.radians(180))            # 3.141592653589793

print(math.asin(1))                 # pi/2 ≈ 1.5707...  – arcsin
print(math.acos(-1))                # pi ≈ 3.1415...     – arccos
print(math.atan(1))                 # pi/4 ≈ 0.7853...   – arctan
print(math.atan2(1, 1))            # pi/4 – atan of y/x (handles quadrants)

# =============================================================
# FACTORIAL, GCD, LCM
# =============================================================

print(math.factorial(5))    # 120  – 5! = 5*4*3*2*1
print(math.factorial(0))    # 1

print(math.gcd(12, 8))      # 4   – greatest common divisor
print(math.gcd(100, 75))    # 25
print(math.lcm(4, 6))       # 12  – least common multiple (Python 3.9+)
print(math.lcm(12, 18))     # 36

# =============================================================
# COMBINATORICS
# =============================================================

print(math.comb(5, 2))       # 10  – "5 choose 2" (combinations, no repeats)
print(math.perm(5, 2))       # 20  – permutations of 2 from 5

# =============================================================
# OTHER USEFUL FUNCTIONS
# =============================================================

print(math.fabs(-5.5))       # 5.5  – float absolute value
print(math.copysign(3, -1))  # -3.0 – copy sign of second arg to first
print(math.hypot(3, 4))      # 5.0  – Euclidean distance sqrt(3²+4²)
print(math.hypot(1, 1, 1))   # sqrt(3) ≈ 1.732 – works in n-dimensions (3.8+)

print(math.isclose(0.1 + 0.2, 0.3))          # True – safe float comparison
print(0.1 + 0.2 == 0.3)                       # False – direct float comparison fails!
print(math.isclose(1.0, 1.0000001, rel_tol=1e-5))  # True

print(math.prod([1, 2, 3, 4, 5]))  # 120  – product of iterable (3.8+)

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Circle geometry ---
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 4), round(circumference, 4)

area, circ = circle(5)
print(f"Area: {area}, Circumference: {circ}")

# --- Hypotenuse ---
def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(hypotenuse(3, 4))    # 5.0

# --- Compound interest ---
def compound_interest(principal, rate, times_per_year, years):
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)

print(round(compound_interest(1000, 0.05, 12, 10), 2))  # 1647.01

# --- Digits in a number ---
def count_digits(n):
    return math.floor(math.log10(abs(n))) + 1

print(count_digits(12345))   # 5
print(count_digits(1))       # 1
