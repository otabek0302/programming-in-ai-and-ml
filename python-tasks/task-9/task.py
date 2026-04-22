# =============================================================
# Topics: functions, loops, strings, lists, error handling
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Leap Year Checker
# -------------------------------------------------------------
# A year is a leap year if:
#   - Divisible by 4    AND
#   - NOT divisible by 100, UNLESS also divisible by 400.
#
# 1. Write a function  is_leap_year(year)  that returns True/False.
# 2. Test with: 2000, 1900, 2024, 2023, 1600.
# 3. Print all leap years between 2000 and 2050.
# 4. Count how many leap years are in the 20th century (1901–2000).
# 5. Find the next leap year after a given year  next_leap(year).
#    Test with: 2023, 2024, 2100.


# -------------------------------------------------------------
# TASK 2 – Remove Duplicates (Order-Preserving)
# -------------------------------------------------------------
# 1. Write a function  unique_ordered(items)  that removes duplicates
#    while keeping the FIRST occurrence of each item, in original order.
#    Do NOT use dict.fromkeys() or any set-based shortcut —
#    use a loop and a "seen" tracking list.
# 2. Test with:
#       ["a", "b", "a", "c", "b", "d"]  →  ["a", "b", "c", "d"]
#       [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]  →  [3, 1, 4, 5, 9, 2, 6]
# 3. Write a second version  unique_last(items)  that keeps the
#    LAST occurrence instead of the first.
# 4. Test unique_last with the same inputs.
# 5. Compare both outputs side-by-side and confirm they differ
#    where expected.


# -------------------------------------------------------------
# TASK 3 – Number to Words
# -------------------------------------------------------------
# Convert integers 0–99 to their English word form.
# 1. Define lookup dicts/lists for ones and tens words.
# 2. Write a function  number_to_words(n)  that handles:
#       0–19  : "zero", "one", ..., "nineteen"
#       20–99 : "twenty", "twenty-one", ..., "ninety-nine"
#    Raise ValueError for numbers outside 0–99.
# 3. Test every value from 0 to 20.
# 4. Test: 42, 55, 73, 99.
# 5. Write a function  words_to_number(words)  that reverses the
#    conversion for the same 0–99 range and verify it is the
#    inverse of number_to_words for 0–20.


# -------------------------------------------------------------
# TASK 4 – Command-Line Calculator
# -------------------------------------------------------------
# Build a calculator that processes string expressions.
# 1. Write a function  calculate(expression)  that accepts strings
#    like "10 + 5", "8 * 3", "20 / 4", "15 - 7".
#    Split on spaces to get: left operand, operator, right operand.
# 2. Support operators: +, -, *, /, // (floor div), % (modulo), ** (power).
# 3. Raise ValueError for unknown operators.
# 4. Raise ZeroDivisionError for division by zero.
# 5. Test with 7 expressions covering all operators, plus 2 error cases,
#    wrapping each call in a try/except for clean error output.


# -------------------------------------------------------------
# TASK 5 – Group Words by First Letter
# -------------------------------------------------------------
# Given:  words = ["apple", "banana", "avocado", "blueberry",
#                  "cherry", "apricot", "coconut", "cranberry"]
# 1. Write a function  group_by_letter(words)  that returns a dict
#    where each key is a letter and the value is a sorted list of
#    words starting with that letter.
# 2. Print each group on its own line:  "a: apple, apricot, avocado"
# 3. Find and print the letter that has the most words.
# 4. Write a second function  group_by_length(words)  that groups
#    words by their character length instead of first letter.
# 5. Print the group_by_length output and find the most common length.
