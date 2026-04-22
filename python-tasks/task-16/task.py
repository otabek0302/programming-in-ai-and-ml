# =============================================================
# Topics: operators, booleans, conditionals, while loops, casting
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Operator Deep Dive
# -------------------------------------------------------------
# 1. Given a = 17 and b = 5, compute and print the result of:
#       +, -, *, /, //, %, ** for the pair.
#    Label each line: e.g. "17 // 5 = 3"
# 2. Demonstrate all comparison operators (==, !=, <, >, <=, >=)
#    for the same pair, printing each as a boolean result.
# 3. Demonstrate all bitwise operators (&, |, ^, ~, <<, >>)
#    for a = 0b1010 (10) and b = 0b1100 (12).
#    Print both the binary and decimal results.
# 4. Use augmented assignment operators (+=, -=, *=, //=, %=)
#    in sequence starting from x = 100. Print x after each step.
# 5. Show operator precedence with 3 ambiguous expressions and
#    print both the Python result and your expected result with explanation.


# -------------------------------------------------------------
# TASK 2 – Truthiness Explorer
# -------------------------------------------------------------
# 1. Print whether each of the following is truthy or falsy using bool():
#       0, 1, -1, 0.0, 0.1, "", "0", " ", [], [0], {}, {"a":1}, None, False, True
# 2. Write a function  describe(value)  that prints:
#       "<value> is TRUTHY" or "<value> is FALSY"
#    Call it for each item above.
# 3. Write a function  first_truthy(*values)  that returns the first
#    truthy value in the arguments, or None if all are falsy.
# 4. Write a function  all_truthy(*values)  and  any_truthy(*values)
#    without using Python's built-in all() or any().
# 5. Test all_truthy and any_truthy with 3 different argument lists.


# -------------------------------------------------------------
# TASK 3 – Chained Conditionals
# -------------------------------------------------------------
# 1. Write a function  bmi_category(weight_kg, height_m)  that computes
#    BMI = weight / height² and returns:
#       BMI < 18.5  → "Underweight"
#       18.5–24.9   → "Normal"
#       25.0–29.9   → "Overweight"
#       >= 30       → "Obese"
# 2. Test with 5 different (weight, height) pairs.
# 3. Write a function  day_type(day)  that returns "Weekday" or "Weekend"
#    for a given day name (case-insensitive). Raise ValueError for invalid names.
# 4. Write a function  season(month)  that returns the season name
#    for a given month number (1–12). Raise ValueError for invalid months.
# 5. Test day_type and season with valid and invalid inputs.


# -------------------------------------------------------------
# TASK 4 – While Loop Patterns
# -------------------------------------------------------------
# 1. Use a while loop to print all powers of 2 that are less than 1000
#    (1, 2, 4, 8, ... , 512). Count and print how many there are.
# 2. Use a while loop to find the smallest n where n! > 1,000,000.
#    Print n and n!.
# 3. Use a while loop to implement the Collatz sequence for a starting
#    number of 27:
#       If even: n = n / 2.    If odd: n = 3n + 1.   Stop when n = 1.
#    Print the full sequence and how many steps it took.
# 4. Use a while loop to sum digits of a number repeatedly until
#    a single digit remains (digital root).  Test with 9875.
# 5. Use a while loop to find the GCD of two numbers using
#    the Euclidean algorithm.  Test: gcd(48, 18) → 6, gcd(100, 75) → 25.


# -------------------------------------------------------------
# TASK 5 – Ternary and Short-Circuit
# -------------------------------------------------------------
# 1. Rewrite these if/else blocks as single-line ternary expressions:
#       a) If x > 0, label = "positive", else label = "non-positive"
#       b) If items list is non-empty, result = items[0], else result = "none"
#       c) If score >= 60, status = "pass", else status = "fail"
# 2. Print the result of each ternary for 3 different input values.
# 3. Demonstrate short-circuit evaluation:
#       a) Show that  False and <expr>  never evaluates <expr>
#          by using a function that prints a side effect.
#       b) Show that  True or <expr>  never evaluates <expr>.
# 4. Write a function  clamp(value, low, high)  that returns value
#    constrained between low and high using only ternary expressions.
# 5. Test clamp(15, 0, 10) → 10,  clamp(-5, 0, 10) → 0,  clamp(7, 0, 10) → 7.
