# =============================================================
# Topics: loops, functions, string analysis, tuples, dictionaries
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Fibonacci Generator
# -------------------------------------------------------------
# 1. Write a function  fibonacci(n)  that returns a list of
#    the first n Fibonacci numbers (starting from 0).
# 2. Print the sequence for n=15.
# 3. Write a second function  fibonacci_sum(n)  that returns
#    the sum of the first n Fibonacci numbers.
#    Verify: fib_sum(n) == fib(n+2) - 1  for n = 5, 10, 15.
# 4. Find and print the first Fibonacci number greater than 1000.
# 5. Print all Fibonacci numbers up to 500 that are also even.


# -------------------------------------------------------------
# TASK 2 – Text Analyser
# -------------------------------------------------------------
# Write your own paragraph (at least 4 sentences) and store it as a string.
# 1. Count the number of sentences (split on ".", "!", "?").
# 2. Count the total number of words.
# 3. Count the total number of characters (excluding spaces).
# 4. Calculate the average word length (rounded to 2 decimal places).
# 5. Find the longest word and the shortest word (ignore punctuation).
#    Print a summary report with all five results.


# -------------------------------------------------------------
# TASK 3 – Sort List of Tuples
# -------------------------------------------------------------
# Given:  people = [("Charlie", 30), ("Alice", 25), ("Bob", 25), ("Dave", 35)]
# 1. Sort the list by age (ascending). Print the result.
# 2. Sort by age descending. Print the result.
# 3. Sort by name alphabetically. Print the result.
# 4. Sort by age ascending, with ties broken by name alphabetically.
#    Print the result.
# 5. Write a function  oldest_and_youngest(people)  that returns
#    a tuple of (oldest_name, youngest_name). Test it.


# -------------------------------------------------------------
# TASK 4 – Duplicate Finder
# -------------------------------------------------------------
# 1. Write a function  find_duplicates(items)  that returns a list
#    of values that appear more than once in the input list.
#    The result should contain each duplicate only once, sorted.
# 2. Test with: [1, 2, 3, 2, 4, 3, 5, 1, 1]  →  [1, 2, 3]
# 3. Write a function  remove_duplicates(items)  that removes all
#    duplicate occurrences while preserving the original order.
#    Do NOT use a set directly — use a loop and a seen list.
# 4. Test: [4, 1, 2, 1, 3, 2, 4]  →  [4, 1, 2, 3]
# 5. Write a function  duplicate_count(items)  that returns a dict
#    mapping each duplicate value to how many times it appears.


# -------------------------------------------------------------
# TASK 5 – Grade Book
# -------------------------------------------------------------
# Build a grade book for a class using a list of dicts.
# Each student dict: {"name": str, "scores": list[int]}
#
# 1. Write  add_student(gradebook, name)  – adds a student with empty scores.
#    Raise ValueError if name already exists.
# 2. Write  add_score(gradebook, name, score)  – appends a score (0–100).
#    Raise ValueError if score is out of range or student not found.
# 3. Write  student_average(gradebook, name)  – returns the average score.
# 4. Write  class_statistics(gradebook)  – returns a dict with:
#       "highest_avg", "lowest_avg", "class_avg", "top_student", "lowest_student"
# 5. Pre-load 4 students with 3-5 scores each, then print a full report
#    using class_statistics() and each student's name + average + letter grade.
