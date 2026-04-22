# =============================================================
# Topics: dictionaries, comprehensions, sorting, functions, loops
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Dictionary Merge and Update
# -------------------------------------------------------------
# Given:
#   defaults = {"theme": "light", "language": "en", "font_size": 14}
#   user_prefs = {"theme": "dark", "font_size": 18, "notifications": True}
# 1. Merge the two dicts so user_prefs values override defaults.
#    Do this THREE ways: using update(), using {**a, **b}, using | (Python 3.9+).
# 2. Print the merged result for each approach.
# 3. Confirm all three produce the same output (True/False).
# 4. Add a new key "last_updated" with value "2025-01-01" to the merged dict.
# 5. Print only the keys that differ between defaults and user_prefs.


# -------------------------------------------------------------
# TASK 2 – Invert a Dictionary
# -------------------------------------------------------------
# Given:  grades = {"Alice": "A", "Bob": "B", "Carol": "A", "Dave": "C", "Eve": "B"}
# 1. Write a function  invert(d)  that swaps keys and values.
#    Since multiple students can share a grade, the inverted dict should map
#    each grade to a LIST of student names.
#    e.g. {"A": ["Alice", "Carol"], "B": ["Bob", "Eve"], "C": ["Dave"]}
# 2. Print the inverted dict.
# 3. Sort the student list under each grade alphabetically.
# 4. Print how many students received each grade.
# 5. Print the grade that the most students received.


# -------------------------------------------------------------
# TASK 3 – Dictionary Comprehension
# -------------------------------------------------------------
# 1. Create a dict comprehension that maps numbers 1–10 to their cubes.
# 2. Create a dict comprehension from a list of words that maps each word
#    to its length.  words = ["python", "is", "fun", "and", "powerful"]
# 3. Filter the word-length dict to keep only words longer than 3 characters.
# 4. Create a dict comprehension that maps each letter in "programming"
#    to the number of times it appears (character frequency).
# 5. From the frequency dict, print only letters that appear more than once,
#    sorted by frequency descending.


# -------------------------------------------------------------
# TASK 4 – Nested Dictionary – School Records
# -------------------------------------------------------------
# Build a nested dict:  school = { class_name: { student: grade } }
# 1. Pre-load 3 classes ("10A", "10B", "10C") with 3 students each
#    and their scores (0–100).
# 2. Write a function  class_average(school, class_name)  that returns
#    the average score for a class.
# 3. Write a function  top_student(school)  that returns the name and
#    score of the student with the highest score across ALL classes.
# 4. Print the average score for each class.
# 5. Print the name of the top student and which class they are in.


# -------------------------------------------------------------
# TASK 5 – Word Index Builder
# -------------------------------------------------------------
# Given a multi-line text (write your own, at least 3 lines):
# 1. Split the text into words (strip punctuation, lowercase).
# 2. Build an index dict: each key is a word, value is a list of
#    line numbers (1-based) where that word appears.
#    e.g. {"python": [1, 3], "is": [1, 2]}
# 3. Print the full index sorted alphabetically by word.
# 4. Print all words that appear on more than one line.
# 5. Print the word that appears on the most lines.
