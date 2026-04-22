# =============================================================
# PYTHON ARRAYS
# =============================================================

# Python does not have a built-in "array" type the way C or Java does.
# For basic ordered collections, Python uses LISTS (covered in 11_lists).
# For true arrays (fixed type, memory-efficient), Python provides:
#   - array module  (built-in, typed arrays)
#   - numpy arrays  (third-party, industry standard for numerical work)

# =============================================================
# LISTS AS ARRAYS
# =============================================================

# In everyday Python code, lists are used as arrays.
cars = ["Ford", "Volvo", "BMW"]

print(cars[0])          # Ford      – access by index
print(len(cars))        # 3         – length

cars[0] = "Toyota"      # modify
print(cars)

cars.append("Honda")    # add to end
print(cars)

cars.pop(1)             # remove by index
print(cars)

for car in cars:
    print(car)

# =============================================================
# array MODULE  (built-in, typed, memory-efficient)
# =============================================================

import array

# array.array(typecode, initializer)
# Typecodes: 'i' = int, 'f' = float, 'd' = double, 'b' = signed char, etc.

nums = array.array("i", [1, 2, 3, 4, 5])
print(nums)               # array('i', [1, 2, 3, 4, 5])
print(type(nums))         # <class 'array.array'>
print(nums[0])            # 1
print(nums[-1])           # 5

# All values must be the same type
# nums.append("hello")   # TypeError

nums.append(6)
print(nums)

nums.insert(0, 0)
print(nums)

nums.remove(3)            # remove first occurrence of value 3
print(nums)

popped = nums.pop(1)      # remove by index
print(popped, nums)

print(nums.index(4))      # index of first occurrence
print(nums.count(2))      # count occurrences

# Slice
print(nums[1:4])          # returns a new array

# Loop
for n in nums:
    print(n, end=" ")
print()

# Common typecodes:
# 'b' – signed char      (1 byte,  int)
# 'B' – unsigned char    (1 byte,  int)
# 'i' – signed int       (2+ bytes, int)
# 'I' – unsigned int     (2+ bytes, int)
# 'l' – signed long      (4+ bytes, int)
# 'f' – float            (4 bytes, float)
# 'd' – double           (8 bytes, float)

floats = array.array("f", [1.1, 2.2, 3.3])
print(floats)

# =============================================================
# numpy ARRAYS  (install: pip install numpy)
# =============================================================

# numpy is the standard for numerical and scientific computing.
# numpy arrays are faster than lists for large numerical data,
# support vectorised operations, and are the foundation of
# pandas, scikit-learn, TensorFlow, and most ML libraries.

try:
    import numpy as np

    # --- Creating arrays ---
    a = np.array([1, 2, 3, 4, 5])
    print(a)                # [1 2 3 4 5]
    print(type(a))          # <class 'numpy.ndarray'>
    print(a.dtype)          # int64
    print(a.shape)          # (5,)
    print(a.ndim)           # 1

    # 2D array (matrix)
    matrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    print(matrix)
    print(matrix.shape)     # (3, 3)
    print(matrix.ndim)      # 2

    # --- Creation helpers ---
    print(np.zeros((2, 3)))         # 2x3 array of 0.0
    print(np.ones((2, 3)))          # 2x3 array of 1.0
    print(np.full((2, 3), 7))       # 2x3 array filled with 7
    print(np.eye(3))                # 3x3 identity matrix
    print(np.arange(0, 10, 2))      # [0 2 4 6 8]  – like range()
    print(np.linspace(0, 1, 5))     # [0. 0.25 0.5 0.75 1.] – evenly spaced

    # --- Indexing & slicing ---
    a = np.array([10, 20, 30, 40, 50])
    print(a[0])         # 10
    print(a[-1])        # 50
    print(a[1:4])       # [20 30 40]
    print(a[::2])       # [10 30 50]

    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m[0, 0])      # 1   – row 0, col 0
    print(m[1, 2])      # 6   – row 1, col 2
    print(m[:, 1])      # [2 5 8]  – entire column 1
    print(m[0, :])      # [1 2 3]  – entire row 0

    # --- Vectorised arithmetic (no loops needed) ---
    a = np.array([1, 2, 3, 4, 5])
    print(a + 10)           # [11 12 13 14 15]
    print(a * 2)            # [ 2  4  6  8 10]
    print(a ** 2)           # [ 1  4  9 16 25]

    b = np.array([10, 20, 30, 40, 50])
    print(a + b)            # [11 22 33 44 55]
    print(a * b)            # [ 10  40  90 160 250]

    # --- Aggregate functions ---
    print(a.sum())          # 15
    print(a.min())          # 1
    print(a.max())          # 5
    print(a.mean())         # 3.0
    print(a.std())          # standard deviation
    print(np.median(a))     # 3.0

    # --- Boolean indexing (filtering) ---
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a[a > 3])         # [4 5 6]
    print(a[a % 2 == 0])    # [2 4 6]

    # --- Shape manipulation ---
    a = np.arange(1, 10)
    print(a.reshape(3, 3))  # reshape to 3x3 matrix
    print(a.reshape(9, 1))  # column vector

    # --- numpy vs list: speed ---
    # For large numeric data, numpy operations are 10-100x faster
    # because they are implemented in C and avoid Python loop overhead.

except ImportError:
    print("numpy is not installed. Run: pip install numpy")
    print("numpy is essential for data science and machine learning.")

# =============================================================
# LIST vs array.array vs numpy.array
# =============================================================

# list
#   - Built-in, no import
#   - Can hold mixed types
#   - Flexible (append, remove, etc.)
#   - Slower for numerical operations
#   - Use for: general-purpose collections

# array.array
#   - Built-in module
#   - Single type only (typecode required)
#   - More memory-efficient than list for numbers
#   - Use for: storing large amounts of a single numeric type
#              without needing numpy

# numpy.ndarray
#   - Third-party (pip install numpy)
#   - Single type, N-dimensional
#   - Extremely fast vectorised operations
#   - Foundation of scientific Python (pandas, scikit-learn, etc.)
#   - Use for: all numerical / mathematical / ML work
