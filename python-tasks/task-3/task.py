# =============================================================
# Topics: functions, list comprehensions, tuples, sets, while loops
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Find Max Without max()
# -------------------------------------------------------------
# 1. Write a function  find_max(numbers)  that accepts a list of numbers.
# 2. Find the largest number using a loop — do NOT use max() or sorted().
# 3. Return the largest number.
# 4. Test it with: [4, 17, 2, 9, 31, 5]  →  expected: 31
# 5. Handle the edge case where the list is empty: return None and print a message.


# -------------------------------------------------------------
# TASK 2 – List Comprehension Pipeline
# -------------------------------------------------------------
# Given:  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Use a list comprehension to create a list of only the even numbers.
# 2. Use another list comprehension to square each even number.
# 3. Use a third list comprehension to keep only squares greater than 20.
# 4. Print each resulting list on its own line with a label.
# 5. Do all three steps in a single chained list comprehension and print the result.


# -------------------------------------------------------------
# TASK 3 – Palindrome Checker
# -------------------------------------------------------------
# 1. Write a function  is_palindrome(text)  that returns True/False.
# 2. The check must be case-insensitive and ignore spaces.
# 3. Test with: "racecar", "A man a plan a canal Panama", "hello".
# 4. Write a second function  find_palindromes(words)  that filters
#    a list and returns only the palindromes.
# 5. Test find_palindromes with at least 6 words.


# -------------------------------------------------------------
# TASK 4 – Coordinate Distance
# -------------------------------------------------------------
# 1. Create two tuples representing 2D points:  p1 = (3, 4)  p2 = (7, 1)
# 2. Unpack both tuples into named variables.
# 3. Calculate the Euclidean distance:  d = √((x2-x1)² + (y2-y1)²)
#    Use the math module — do NOT hardcode the formula result.
# 4. Print the distance rounded to 2 decimal places.
# 5. Write a function  distance(p1, p2)  that works for any two points
#    and test it with three different pairs.


# -------------------------------------------------------------
# TASK 5 – Word Frequency Counter
# -------------------------------------------------------------
# Given:  text = "the cat sat on the mat the cat sat"
# 1. Split the text into a list of words.
# 2. Build a dictionary where each key is a word and the value is its count.
#    Do this with a loop — do NOT use Counter from collections.
# 3. Print all word-count pairs sorted alphabetically by word.
# 4. Print the word that appears most often.
# 5. Print all words that appear exactly once.
