# =============================================================
# Topics: functions, recursion, error handling, numbers, math
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Power and Root Calculator
# -------------------------------------------------------------
# 1. Write a function  power(base, exp)  that calculates base^exp
#    using a loop — do NOT use ** or math.pow.
# 2. Write a function  integer_sqrt(n)  that returns the integer
#    square root of n (largest integer k where k*k <= n).
#    Do NOT use math.sqrt or ** 0.5 — use a loop.
# 3. Test power(2, 10), power(3, 5), power(5, 0).
# 4. Test integer_sqrt for: 25, 26, 100, 101, 1, 0.
# 5. Raise ValueError in power() if exp is negative,
#    and in integer_sqrt() if n is negative.


# -------------------------------------------------------------
# TASK 2 – Recursive Sum and Count
# -------------------------------------------------------------
# 1. Write a recursive function  sum_digits(n)  that returns the
#    sum of all digits of a non-negative integer.
#    e.g. sum_digits(1234)  →  10
# 2. Write a recursive function  count_digits(n)  that returns the
#    number of digits.
#    e.g. count_digits(1234)  →  4
# 3. Write a recursive function  reverse_number(n)  that returns the
#    number with its digits reversed.
#    e.g. reverse_number(1234)  →  4321
# 4. Test all three for: 0, 7, 123, 9999, 10000.
# 5. A number is a "digital root" candidate if sum_digits applied
#    repeatedly until single digit gives the number itself.
#    Find all such single-digit results for numbers 1–50.


# -------------------------------------------------------------
# TASK 3 – Safe Division and Math Errors
# -------------------------------------------------------------
# 1. Write a function  safe_divide(a, b)  that returns the result
#    of a / b, or None if b is 0. Print a warning for zero division.
# 2. Write a function  safe_sqrt(n)  that returns √n, or None
#    for negative inputs. Use the math module.
# 3. Write a function  safe_log(n, base=10)  that returns log(n),
#    or None for n <= 0. Use the math module.
# 4. Test each function with 3 valid and 2 invalid inputs.
# 5. Write a function  calculate_all(a, b)  that calls all three
#    safe functions and prints a summary of results for given a, b.


# -------------------------------------------------------------
# TASK 4 – Number Properties
# -------------------------------------------------------------
# 1. Write a function  is_perfect(n)  that returns True if n equals
#    the sum of its proper divisors (e.g. 6 = 1+2+3).
# 2. Write a function  is_abundant(n)  that returns True if the sum
#    of proper divisors is greater than n.
# 3. Write a function  is_deficient(n)  that returns True if the sum
#    is less than n.
# 4. Classify every number from 1 to 30 as perfect, abundant, or deficient.
#    Print each number and its classification.
# 5. Count how many numbers in 1–100 fall into each category and print totals.


# -------------------------------------------------------------
# TASK 5 – Custom Exception Handling
# -------------------------------------------------------------
# 1. Write a function  parse_age(value)  that:
#       - Casts value to int (raise TypeError with message if not possible).
#       - Raises ValueError if age < 0 or age > 130.
#       - Returns the valid age.
# 2. Write a function  parse_score(value)  that:
#       - Casts value to float.
#       - Raises ValueError if score is not between 0.0 and 100.0.
#       - Returns the valid score.
# 3. Test each function with 3 valid and 3 invalid inputs,
#    wrapping every call in try/except and printing the error type + message.
# 4. Write a function  safe_parse(parser_func, value)  that calls
#    any parser function and returns (result, None) on success
#    or (None, error_message) on failure.
# 5. Use safe_parse to process a mixed list of values through parse_age
#    and print a result summary.
