# =============================================================
# Topics: data types, casting, numbers, strings, type checking
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Type Detective
# -------------------------------------------------------------
# Given:  values = [42, 3.14, "hello", True, None, [1,2], {"a":1}, (1,2), {1,2}]
# 1. Loop through values and print each item's type using type().
# 2. Separate them into groups: numbers, sequences, mappings, others.
#    Print each group with its items.
# 3. Use isinstance() to check: which items are numeric (int or float)?
#    Print True/False for each item.
# 4. Write a function  type_label(value)  that returns a human-readable
#    string: "integer", "float", "string", "boolean", "list", "dict",
#    "tuple", "set", or "other".
# 5. Call type_label() for all items in values and print the results.


# -------------------------------------------------------------
# TASK 2 – Safe Type Casting
# -------------------------------------------------------------
# 1. Write a function  to_int(value)  that tries to cast value to int.
#    Return the int on success, or None on failure (no crash).
# 2. Write a function  to_float(value)  that does the same for float.
# 3. Test each with: "42", "3.14", "hello", True, False, None, [], "0xFF"
# 4. Write a function  smart_cast(value)  that tries to cast in order:
#    int → float → bool → str, returning the first successful result
#    along with the type name. Print "cast to <type>: <value>".
# 5. Run smart_cast on: "100", "3.14", "True", "hello", 0, None.


# -------------------------------------------------------------
# TASK 3 – Number Base Converter
# -------------------------------------------------------------
# 1. Write a function  to_binary(n)  that converts a non-negative integer
#    to its binary string WITHOUT using bin() — use repeated division by 2.
# 2. Write a function  to_hex(n)  that converts to hexadecimal WITHOUT
#    using hex() — use repeated division by 16 and a lookup string.
# 3. Test both for: 0, 1, 10, 42, 255, 1024.
# 4. Verify your results against bin() and hex() for each test.
# 5. Write a function  from_binary(s)  that converts a binary string
#    back to an integer WITHOUT using int(s, 2) — use a loop.
#    Test that from_binary(to_binary(n)) == n for all test values.


# -------------------------------------------------------------
# TASK 4 – Float Precision and Rounding
# -------------------------------------------------------------
# 1. Demonstrate why 0.1 + 0.2 != 0.3 in Python. Print the actual result.
# 2. Use round() to fix the comparison. Show round(0.1 + 0.2, 10) == 0.3.
# 3. Write a function  round_half_up(n, decimals=0)  that always rounds
#    0.5 upward (Python's built-in round() uses banker's rounding).
#    Test: round_half_up(2.5) → 3, round_half_up(3.5) → 4.
# 4. Write a function  truncate(n, decimals)  that cuts off decimal
#    digits WITHOUT rounding.  e.g. truncate(3.987, 2) → 3.98
# 5. Print a table comparing round(), round_half_up(), and truncate()
#    for values: 1.5, 2.5, 3.45, 4.55, 5.005.


# -------------------------------------------------------------
# TASK 5 – String ↔ Number Conversions
# -------------------------------------------------------------
# 1. Write a function  digits_of(n)  that returns a list of individual
#    digits of a non-negative integer without converting to string.
#    e.g. digits_of(1234) → [1, 2, 3, 4]
# 2. Write a function  from_digits(digits)  that reconstructs the integer
#    from a list of digits.  Verify it is the inverse of digits_of.
# 3. Write a function  is_armstrong(n)  that returns True if n equals
#    the sum of its digits each raised to the power of the digit count.
#    e.g. 153 = 1³ + 5³ + 3³  →  True
# 4. Print all Armstrong numbers between 1 and 1000.
# 5. Write a function  digit_product(n)  that returns the product of
#    all non-zero digits.  e.g. digit_product(1230) → 6  (1×2×3).
#    Test for: 111, 1230, 999, 5, 10000.
