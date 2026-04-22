# =============================================================
# Topics: strings, loops, lists, functions, booleans
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Count Words in a Sentence
# -------------------------------------------------------------
# Given:  sentence = "  Hello   world  this is   Python  "
# 1. Strip leading/trailing spaces and split into words.
# 2. Print the total word count.
# 3. Print each word with its index (starting from 1):
#       1. Hello
#       2. world  ...
# 4. Print the longest and shortest word.
# 5. Print True if all words start with an uppercase letter, False otherwise.


# -------------------------------------------------------------
# TASK 2 – List Rotation Without Built-ins
# -------------------------------------------------------------
# Given:  items = [10, 20, 30, 40, 50]
# 1. Write a function  rotate_left(lst, steps)  that moves each element
#    left by `steps` positions (wrap around).
#    Do NOT use slicing — use a loop to build a new list.
# 2. Test: rotate_left([10,20,30,40,50], 2)  →  [30, 40, 50, 10, 20]
# 3. Write rotate_right(lst, steps) the same way but in the opposite direction.
# 4. Verify that rotate_right(rotate_left(lst, n), n) == lst.
# 5. Test both with steps = 0 and steps larger than the list length.


# -------------------------------------------------------------
# TASK 3 – Build a Multiplication List
# -------------------------------------------------------------
# 1. Write a function  multiples(n, limit)  that returns a list of
#    all multiples of n up to and including limit.
# 2. Test: multiples(3, 30)  →  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 3. Write a function  common_multiples(a, b, limit)  that returns
#    multiples shared by both a and b up to limit.
# 4. Test: common_multiples(3, 4, 50)  →  [12, 24, 36, 48]
# 5. Print the first 5 common multiples of 6 and 8.


# -------------------------------------------------------------
# TASK 4 – String Compression
# -------------------------------------------------------------
# 1. Write a function  compress(s)  that compresses consecutive
#    repeated characters.
#    e.g. "aaabbbccddddee"  →  "a3b3c2d4e2"
#    If a character appears only once, just write the character (no "1").
#    e.g. "abcd"  →  "abcd"
# 2. Write a function  decompress(s)  that reverses the process.
#    e.g. "a3b3c2d4e2"  →  "aaabbbccddddee"
# 3. Verify compress(decompress(compressed)) == compressed for 3 strings.
# 4. Handle edge cases: empty string, single character, no repeats.
# 5. Test with: "aabbcc", "aaabbbccc", "abcde", "zzzzz".


# -------------------------------------------------------------
# TASK 5 – Boolean Expression Evaluator
# -------------------------------------------------------------
# 1. Write a function  check_password(password)  that returns True
#    only if ALL of the following are True:
#       - Length is at least 8 characters.
#       - Contains at least one digit.
#       - Contains at least one uppercase letter.
#       - Contains at least one lowercase letter.
#       - Does not contain spaces.
# 2. Test with 4 passwords: 2 valid, 2 invalid.
# 3. For each invalid password, print which specific rule(s) it broke.
# 4. Write a separate function for each rule that returns True/False.
# 5. Combine all rule functions in check_password using and/or logic.
