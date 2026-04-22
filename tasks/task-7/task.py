# =============================================================
# Topics: strings, dictionaries, loops, functions, error handling
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Phone Number Formatter
# -------------------------------------------------------------
# 1. Store a raw phone number string:  digits = "9981234567"
# 2. Validate it has exactly 10 digits and contains only numbers.
#    Print an error message and stop if invalid.
# 3. Format it as:  "(998) 123-4567"  using string slicing.
# 4. Write a function  format_phone(digits)  that does steps 2–3.
# 5. Test with 3 valid and 2 invalid inputs.


# -------------------------------------------------------------
# TASK 2 – To-Do List Manager
# -------------------------------------------------------------
# Build a to-do list using a list of dicts.
# Each task dict has: "id" (int), "title" (str), "done" (bool).
# 1. Write  add_task(tasks, title)  – appends a new task (auto-increment id).
# 2. Write  complete_task(tasks, task_id)  – marks a task as done.
#    Raise ValueError if the id doesn't exist.
# 3. Write  delete_task(tasks, task_id)  – removes a task by id.
# 4. Write  display_tasks(tasks)  – prints all tasks:
#       [✓] 1. Buy groceries
#       [ ] 2. Write code
# 5. Demonstrate all four functions with at least 4 tasks,
#    completing 2 and deleting 1 before the final display.


# -------------------------------------------------------------
# TASK 3 – Sieve of Eratosthenes
# -------------------------------------------------------------
# 1. Write a function  sieve(n)  that returns a list of all prime
#    numbers up to and including n using the Sieve of Eratosthenes.
#    (Create a boolean list, mark composites, collect the Trues.)
# 2. Print all primes up to 50.
# 3. Print the count of primes up to 100, 500, and 1000.
# 4. Write a function  is_prime(n)  using trial division (no sieve)
#    and verify it agrees with sieve() for all numbers up to 50.
# 5. Find and print the first 10 twin primes
#    (pairs where p and p+2 are both prime).


# -------------------------------------------------------------
# TASK 4 – FizzBuzz Extended
# -------------------------------------------------------------
# 1. Write a function  fizzbuzz(n, rules)  where rules is a dict
#    mapping divisors to words, e.g. {3: "Fizz", 5: "Buzz", 7: "Whizz"}.
# 2. For each number 1..n, concatenate all matching words in order
#    of divisor (smallest first); if no rule matches, use the number itself.
# 3. Run it for n=30 with rules {3:"Fizz", 5:"Buzz"} and print the results.
# 4. Run it again with rules {3:"Fizz", 5:"Buzz", 7:"Whizz"} for n=21.
# 5. Count and print how many numbers in 1..100 are pure numbers
#    (no rule matched) using the {3,5} rule set.


# -------------------------------------------------------------
# TASK 5 – Multi-Unit Temperature Converter
# -------------------------------------------------------------
# Supported scales: Celsius, Fahrenheit, Kelvin.
# Formulas:
#   C → F: F = C * 9/5 + 32     F → C: C = (F - 32) * 5/9
#   C → K: K = C + 273.15       K → C: C = K - 273.15
#
# 1. Write a function  convert(value, from_scale, to_scale)
#    that converts between any two of the three scales.
#    Use "C", "F", "K" as scale identifiers (case-insensitive).
#    Raise ValueError for unknown scales.
# 2. Test: 100°C → F, 32°F → C, 300K → C, 0°C → K.
# 3. Write a function  convert_all(value, from_scale)
#    that returns a dict with the value in all three scales.
# 4. Print a nicely formatted conversion table for 0, 20, 37, 100°C.
# 5. Add a physical limit: raise ValueError if the result is below
#    absolute zero (−273.15°C / 0K / −459.67°F).
