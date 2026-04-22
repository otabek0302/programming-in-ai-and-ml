# =============================================================
# Topics: lambda, dictionaries, recursion, string manipulation, data parsing
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Lambda Pipeline
# -------------------------------------------------------------
# Given:  words = ["hi", "Python", "is", "awesome", "code", "AI", "learning"]
# 1. Use filter() + lambda to keep only words with 4 or more characters.
# 2. Use map() + lambda to convert the filtered words to UPPERCASE.
# 3. Use sorted() + lambda to sort the result by length (shortest first),
#    breaking ties alphabetically.
# 4. Print the final list.
# 5. Redo steps 1–3 as a single expression using nested map/filter/sorted
#    and print the result to confirm it matches.


# -------------------------------------------------------------
# TASK 2 – Product Inventory Manager
# -------------------------------------------------------------
# Build an inventory system using a dictionary of dictionaries.
# Structure:  { product_name: { "price": float, "stock": int } }
#
# 1. Start with 4 products pre-loaded.
# 2. Write a function  add_product(inventory, name, price, stock)
#    that adds a new product (raise ValueError if it already exists).
# 3. Write a function  update_stock(inventory, name, quantity)
#    that adds or removes stock (raise ValueError if stock goes below 0).
# 4. Write a function  total_value(inventory)  that returns the total
#    value of all stock  (price × stock for each product, summed).
# 5. Print a formatted inventory table and the total value.


# -------------------------------------------------------------
# TASK 3 – Flatten Nested List
# -------------------------------------------------------------
# 1. Write a recursive function  flatten(nested)  that takes a list
#    which may contain integers or other lists (any depth) and returns
#    a single flat list of all integers.
# 2. Test with:
#       [1, [2, 3], [4, [5, [6]]]]          → [1, 2, 3, 4, 5, 6]
#       [[1, [2]], [3, [4, [5]]]]            → [1, 2, 3, 4, 5]
#       [1, 2, 3]                            → [1, 2, 3]
# 3. After flattening each list, print the sum and the maximum value.
# 4. Write a second version  flatten_iter(nested)  using a stack (list)
#    instead of recursion — no recursive calls allowed.
# 5. Verify both versions produce the same output for all test cases.


# -------------------------------------------------------------
# TASK 4 – Caesar Cipher
# -------------------------------------------------------------
# 1. Write a function  encode(text, shift)  that shifts every letter
#    in text by shift positions (wrapping around A↔Z and a↔z).
#    Non-letter characters must remain unchanged.
# 2. Write a function  decode(text, shift)  that reverses the encoding.
# 3. Test encode("Hello, World!", 3)  →  "Khoor, Zruog!"
# 4. Test that decode(encode(text, shift), shift) == text for any text/shift.
# 5. Write a function  brute_force(cipher_text)  that prints all 25 possible
#    decoded versions of the ciphertext (shifts 1–25), one per line.


# -------------------------------------------------------------
# TASK 5 – CSV String Parser
# -------------------------------------------------------------
# Given this multi-line string:
#   data = """name,age,city
#   Alice,30,New York
#   Bob,25,London
#   Carol,35,Tokyo"""
#
# 1. Split the data into lines and extract the header row.
# 2. Parse each remaining line into a dictionary using the headers as keys.
#    Cast age to int.
# 3. Store all records in a list of dicts.
# 4. Print each record as:  "Alice (30) – New York"
# 5. Sort the records by age (youngest first) and print the sorted list.
