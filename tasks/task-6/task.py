# =============================================================
# Topics: data structures, sorting, string validation, algorithms
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Stack Implementation
# -------------------------------------------------------------
# Implement a stack using only a Python list (no classes, just functions).
# 1. Write these functions: push(stack, item), pop(stack), peek(stack),
#    is_empty(stack), size(stack).
#    - pop() must raise IndexError on an empty stack.
#    - peek() must raise IndexError on an empty stack.
# 2. Using your stack, write a function  is_balanced(expression)
#    that checks if brackets are balanced in a string.
#    e.g. "({[]})"  → True,   "({)}"  → False,   "((("  → False
# 3. Test is_balanced with at least 5 expressions.
# 4. Write a function  reverse_string(s)  that uses the stack
#    functions to reverse a string (no slicing allowed).
# 5. Test reverse_string with 3 different strings and verify the result.


# -------------------------------------------------------------
# TASK 2 – Top N Students
# -------------------------------------------------------------
# Given a list of dicts:  [{"name": "Alice", "score": 88}, ...]
# 1. Write a function  top_students(students, n)  that returns
#    the top n students sorted by score (highest first).
#    Use sorted() with a key — do NOT use a loop to sort.
# 2. In case of a tie in score, sort alphabetically by name.
# 3. Print each top student as:  "#1  Alice     – 95"  (formatted columns).
# 4. Write a function  pass_or_fail(students, passing_score)
#    that splits the list into two lists: passed and failed.
# 5. Print the count and names of each group.


# -------------------------------------------------------------
# TASK 3 – Advanced Word Frequency
# -------------------------------------------------------------
# Given a paragraph (at least 5 sentences, write your own):
# 1. Clean the text: lowercase, remove punctuation using str methods only
#    (no regex, no imports).
# 2. Build a word frequency dictionary using a loop.
# 3. Print the top 5 most frequent words with their counts,
#    sorted by count descending, then alphabetically for ties.
# 4. Print all words that appear more than once.
# 5. Print the total unique word count and the total word count.


# -------------------------------------------------------------
# TASK 4 – Email Validator
# -------------------------------------------------------------
# Write a function  is_valid_email(email)  using only string methods.
# Rules:
#   - Must contain exactly one "@".
#   - The part before "@" must be at least 1 character.
#   - The part after "@" must contain at least one "." .
#   - The domain (after "@") must have at least 2 chars before "."
#     and at least 2 chars after the last ".".
#   - No spaces allowed anywhere.
# 1. Implement the function following all rules.
# 2. Test with 5 valid and 5 invalid email addresses.
# 3. Print "VALID" or "INVALID" for each test case.
# 4. Write a function  extract_domain(email)  that returns the domain
#    part (e.g. "gmail.com") — only call it for valid emails.
# 5. Print the domain for each valid test email.


# -------------------------------------------------------------
# TASK 5 – Binary Search
# -------------------------------------------------------------
# 1. Write a function  binary_search(sorted_list, target)
#    that returns the index of target, or -1 if not found.
#    Implement it with a while loop — no recursion allowed here.
# 2. Write a second version  binary_search_recursive(sorted_list, target, low, high)
#    using recursion.
# 3. Test both versions with:
#       sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91]
#       targets = [23, 2, 91, 10, 67]
# 4. Verify both functions return the same result for all targets.
# 5. Count how many comparisons each version makes and print the count
#    alongside each result.
