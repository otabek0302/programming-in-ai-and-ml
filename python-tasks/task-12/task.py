# =============================================================
# Topics: tuples, sets, lists, comprehensions, unpacking
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Tuple Unpacking Practice
# -------------------------------------------------------------
# 1. Create a tuple:  person = ("Alice", 28, "Engineer", "Tashkent")
# 2. Unpack it into four named variables and print each on its own line.
# 3. Create a list of 5 similar tuples (name, age, job, city).
# 4. Use a for loop to unpack each tuple and print:
#       "Alice, 28 – Engineer from Tashkent"
# 5. Sort the list by age (ascending) using sorted() with a key,
#    then print the sorted results.


# -------------------------------------------------------------
# TASK 2 – Set Operations
# -------------------------------------------------------------
# Given two lists of student names:
#   class_a = ["Alice", "Bob", "Carol", "Dave", "Eve"]
#   class_b = ["Bob", "Dave", "Frank", "Grace", "Alice"]
# 1. Convert both lists to sets.
# 2. Print students who are in BOTH classes (intersection).
# 3. Print students who are in ONLY class_a (difference).
# 4. Print ALL unique students across both classes (union).
# 5. Print whether class_a and class_b have any students in common (True/False)
#    and the count of shared students.


# -------------------------------------------------------------
# TASK 3 – Flatten and Deduplicate
# -------------------------------------------------------------
# Given:  nested = [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8]]
# 1. Flatten the list into one list using a list comprehension.
# 2. Remove duplicates while preserving the original order (use a loop).
# 3. Print both the flat list and the deduplicated list.
# 4. Convert the deduplicated list to a sorted tuple.
# 5. Print the tuple and check whether 7 is in it (True/False).


# -------------------------------------------------------------
# TASK 4 – Zip and Unzip
# -------------------------------------------------------------
# Given:
#   names  = ["Alice", "Bob", "Carol"]
#   scores = [88, 72, 95]
#   grades = ["B", "C", "A"]
# 1. Use zip() to combine all three into a list of tuples.
# 2. Print each combined tuple.
# 3. Add a fourth student manually to the zipped list as a tuple.
# 4. Sort the zipped list by score descending.
# 5. "Unzip" the sorted list back into three separate lists using zip(*)
#    and print each list with its label.


# -------------------------------------------------------------
# TASK 5 – List Comprehension Shapes
# -------------------------------------------------------------
# 1. Use a list comprehension to generate a list of all (x, y) pairs
#    where x ∈ [1..4] and y ∈ [1..4] and x != y.
# 2. Print all pairs and the total count.
# 3. Use a list comprehension to create a list of squares of odd numbers
#    from 1 to 20.
# 4. Use a list comprehension to filter a list of words and keep only
#    those that are longer than 4 characters and start with a vowel.
#    Test with: ["apple", "in", "orange", "is", "umbrella", "out", "elephant"]
# 5. Chain two list comprehensions: from numbers 1–50, keep those
#    divisible by 3 or 5, then square them.
