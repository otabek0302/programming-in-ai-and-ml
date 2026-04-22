# =============================================================
# Topics: for loops, range, iterators, enumerate, zip, functions
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Range Patterns
# -------------------------------------------------------------
# 1. Using range(), print:
#       a) Numbers 1 to 20 (inclusive).
#       b) Even numbers from 2 to 30.
#       c) Odd numbers from 1 to 19 in reverse (19, 17, ..., 1).
#       d) Multiples of 7 from 0 to 70.
# 2. Use range() to build a list of all two-digit numbers divisible by 9.
# 3. Use range() in reverse to print the countdown: 10, 9, 8 ... 1, Blast off!
# 4. Write a function  sum_range(start, stop, step=1)  that returns the
#    sum of all numbers produced by range(start, stop, step).
#    Test it against the built-in sum(range(...)) to verify.
# 5. Print a right-angled triangle of stars with height 6:
#       *
#       **
#       ***  ...  (using nested range loops, not hardcoded strings)


# -------------------------------------------------------------
# TASK 2 – Enumerate and Zip Together
# -------------------------------------------------------------
# Given:
#   subjects = ["Math", "Science", "English", "History"]
#   scores   = [88, 74, 92, 65]
# 1. Use zip() to pair each subject with its score and print:
#       Math: 88
# 2. Use enumerate() + zip() to add a 1-based rank column:
#       1. Math: 88
# 3. Use zip() to find the subject with the highest score without
#    using max() — use a loop.
# 4. Add a third list: teachers = ["Mr. A", "Ms. B", "Mr. C", "Ms. D"]
#    Zip all three and print a formatted 3-column table.
# 5. Use zip() to create a dictionary mapping subject → score,
#    then print it sorted by score descending.


# -------------------------------------------------------------
# TASK 3 – Nested Loop Patterns
# -------------------------------------------------------------
# 1. Print a 5×5 grid of coordinates (row, col) where both start at 1.
#       (1,1) (1,2) ... (1,5)
#       (2,1) ...
# 2. Print a hollow rectangle of stars (5 wide, 4 tall):
#       *****
#       *   *
#       *   *
#       *****
# 3. Print Pascal's Triangle for the first 7 rows.
#    (Each row: [1], [1,1], [1,2,1], ...)
# 4. Use nested loops to find all pairs (a, b) from 1–10 where
#    a * b == 24.  Print each pair once (avoid (a,b) and (b,a) duplicates).
# 5. Use nested loops to print a pattern:
#       1
#       1 2
#       1 2 3
#       1 2 3 4
#       1 2 3 4 5


# -------------------------------------------------------------
# TASK 4 – Custom Iterator Usage
# -------------------------------------------------------------
# 1. Use iter() and next() to manually step through
#    the list [10, 20, 30, 40, 50].
#    Print each value one at a time and handle StopIteration.
# 2. Write a function  chunked(lst, size)  that uses a loop with
#    range() to yield successive chunks of a list.
#    e.g. chunked([1..10], 3) → [1,2,3], [4,5,6], [7,8,9], [10]
# 3. Test chunked with size 3 on a list of 10 items and print each chunk.
# 4. Use reversed() and enumerate() together to print a list
#    in reverse with its ORIGINAL index:
#    e.g. index 4: "echo", index 3: "delta", ...
# 5. Given a string, use iter() to consume characters one at a time
#    inside a while loop (no for loop, no indexing) and count consonants.


# -------------------------------------------------------------
# TASK 5 – Loop with Accumulator Patterns
# -------------------------------------------------------------
# Given:  numbers = [4, -3, 7, 0, -1, 8, 2, -5, 6, 1]
# 1. In a single loop, compute simultaneously:
#       - sum of all positive numbers
#       - sum of all negative numbers
#       - count of zeros
# 2. Print all three results after the loop.
# 3. In a second loop, build two lists: positives and negatives.
#    Then print the ratio of their sums (handle zero-sum case).
# 4. Find the first pair of adjacent numbers whose product is negative
#    (one positive, one negative). Print their indices and values.
# 5. Print a running total (cumulative sum) of the list as a new list.
#    e.g. [4, 1, 8, 8, 7, 15, ...] — each element is the sum so far.
