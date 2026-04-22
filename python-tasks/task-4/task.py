# =============================================================
# Topics: *args/**kwargs, sets, nested loops, recursion, while loops
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Flexible Stats Function
# -------------------------------------------------------------
# 1. Write a function  stats(*numbers)  that accepts any number of values.
# 2. It should return a dictionary with keys:
#       "count", "sum", "average", "min", "max"
#    Compute all values manually — do NOT use sum(), min(), max().
# 3. Test it with 3 different calls (different number of arguments each time).
# 4. Add a keyword argument  label=""  so the function prints:
#       "Stats for <label>: {...}"
# 5. Handle the case where no numbers are passed: return all zeros.


# -------------------------------------------------------------
# TASK 2 – Unique Words Set
# -------------------------------------------------------------
# Given:  sentence = "To be or not to be that is the question"
# 1. Split the sentence into words (case-insensitive, all lowercase).
# 2. Store the unique words in a set.
# 3. Print the total word count vs. the unique word count.
# 4. Create a second sentence and find:
#       - words that appear in BOTH sentences (intersection)
#       - words that appear only in the FIRST sentence (difference)
# 5. Print both results as sorted lists.


# -------------------------------------------------------------
# TASK 3 – Multiplication Table
# -------------------------------------------------------------
# 1. Use nested for loops to print a multiplication table for 1 through 6.
# 2. Format the output so columns are aligned (use f-string width formatting).
# 3. Print a header row and a separator line.
#    Expected format (partial):
#        ×  │  1   2   3   4   5   6
#       ────┼─────────────────────────
#        1  │  1   2   3   4   5   6
#        2  │  2   4   6   8  10  12
# 4. Highlight (add a "*" suffix) any result that is a perfect square.
# 5. After the table print the count of perfect squares found.


# -------------------------------------------------------------
# TASK 4 – Recursive Factorial & Fibonacci
# -------------------------------------------------------------
# 1. Write a recursive function  factorial(n)  that returns n!
#    Handle n=0 and n=1 as base cases.
# 2. Write a recursive function  fibonacci(n)  that returns
#    the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
# 3. Test factorial for n = 0, 1, 5, 10.
# 4. Test fibonacci for n = 0 through 9 and print the sequence on one line.
# 5. Add a guard in each function to raise a ValueError for negative inputs.


# -------------------------------------------------------------
# TASK 5 – Number Guessing Logic
# -------------------------------------------------------------
# Simulate a number-guessing game WITHOUT using input().
# Use a predefined secret = 42 and a list of guesses = [10, 60, 35, 42, 50].
# 1. Loop through the guesses one by one using a while loop.
# 2. For each guess print: "Too low", "Too high", or "Correct!".
# 3. Stop the loop as soon as the correct answer is found.
# 4. Count how many attempts it took.
# 5. After the loop print: "Found in X attempt(s)" or
#    "Not found after X attempts" if the list runs out.
