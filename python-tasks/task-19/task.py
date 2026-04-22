# =============================================================
# Topics: lambda, map, filter, sorted, functions, lists
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Lambda Basics
# -------------------------------------------------------------
# 1. Write a lambda that takes two numbers and returns the larger one.
#    Test it with (3, 7) and (10, 4).
# 2. Write a lambda that takes a string and returns it reversed.
# 3. Write a lambda that takes a list of numbers and returns the sum
#    of squares.  e.g. [1, 2, 3] → 14
# 4. Write a lambda that takes a dict with "name" and "score" keys
#    and returns a formatted string: "Alice: 88".
# 5. Assign all four lambdas to variables and call each one.
#    Print the result with a descriptive label.


# -------------------------------------------------------------
# TASK 2 – map() in Practice
# -------------------------------------------------------------
# 1. Use map() to convert a list of Celsius temperatures to Fahrenheit.
#    temps_c = [0, 20, 37, 100, -40]
# 2. Use map() to apply str.upper to a list of words.
# 3. Use map() with a lambda to extract the "name" key from a list of dicts.
#    people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
# 4. Use map() with two lists at once: multiply corresponding elements.
#    a = [1, 2, 3, 4]   b = [10, 20, 30, 40]  →  [10, 40, 90, 160]
# 5. Chain two map() calls: first square each number, then convert to string.
#    numbers = [1, 2, 3, 4, 5]  →  ["1", "4", "9", "16", "25"]
#    Print the final list.


# -------------------------------------------------------------
# TASK 3 – filter() in Practice
# -------------------------------------------------------------
# Given:  numbers = [1, -2, 3, -4, 5, -6, 7, 0, -8, 9, 10]
# 1. Use filter() to keep only positive numbers.
# 2. Use filter() to keep only numbers divisible by 3.
# 3. Use filter() with a named function (not lambda) to keep only
#    numbers that are both even AND greater than 4.
# 4. Given a list of strings, use filter() to remove empty strings
#    and strings that contain only spaces.
#    words = ["hello", "", "  ", "world", "", "python", "  "]
# 5. Chain filter() and map(): from numbers 1–20, keep primes,
#    then square them. (Write a simple is_prime function first.)


# -------------------------------------------------------------
# TASK 4 – sorted() with Keys
# -------------------------------------------------------------
# 1. Sort a list of strings by length (shortest first), breaking ties
#    alphabetically.
#    words = ["banana", "fig", "apple", "kiwi", "date", "lime"]
# 2. Sort a list of tuples (name, score) by score descending,
#    then by name ascending for ties.
# 3. Sort a list of dicts by a nested key.
#    employees = [{"name":"Alice","dept":"HR","salary":60000},
#                 {"name":"Bob","dept":"IT","salary":80000},
#                 {"name":"Carol","dept":"HR","salary":75000}]
#    Sort by department first, then by salary descending within each dept.
# 4. Sort a list of strings case-insensitively.
# 5. Write a function  multi_sort(data, *keys)  that sorts a list of
#    dicts by multiple keys in order.  Test it on the employees list.


# -------------------------------------------------------------
# TASK 5 – Combine map, filter, sorted, lambda
# -------------------------------------------------------------
# Given:
#   products = [
#       {"name": "Laptop",  "price": 999.99, "in_stock": True},
#       {"name": "Mouse",   "price":  29.99, "in_stock": False},
#       {"name": "Monitor", "price": 399.99, "in_stock": True},
#       {"name": "Keyboard","price":  79.99, "in_stock": True},
#       {"name": "Webcam",  "price":  49.99, "in_stock": False},
#   ]
# 1. Use filter() to keep only in-stock products.
# 2. Use map() to apply a 10% discount to each in-stock product's price.
#    Return a new dict for each (do NOT mutate the original).
# 3. Use sorted() to sort the discounted products by price ascending.
# 4. Use map() to format each product as: "Laptop – $899.99"
# 5. Print the final list and the total cost of all discounted in-stock items.
