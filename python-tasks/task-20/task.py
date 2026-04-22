# =============================================================
# Topics: strings, lists, dicts, functions, loops, error handling
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Anagram Checker
# -------------------------------------------------------------
# 1. Write a function  is_anagram(a, b)  that returns True if two strings
#    are anagrams of each other (same letters, different order).
#    Ignore spaces and case.  Do NOT use sorted() — use a dict approach.
# 2. Test with: ("listen", "silent"), ("hello", "world"),
#               ("Astronomer", "Moon starer"), ("abc", "ab").
# 3. Write a function  find_anagram_groups(words)  that groups a list
#    of words so that anagrams of each other are in the same group.
# 4. Test with: ["eat", "tea", "tan", "ate", "nat", "bat"]
#    Expected groups: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
# 5. Print each group on its own line sorted alphabetically.


# -------------------------------------------------------------
# TASK 2 – Mini Inventory System
# -------------------------------------------------------------
# Build an inventory using a list of dicts.
# Each item: {"sku": str, "name": str, "price": float, "stock": int}
# 1. Write  add_item(inv, sku, name, price, stock)  – raise ValueError
#    if SKU already exists.
# 2. Write  sell(inv, sku, qty)  – reduce stock by qty.
#    Raise ValueError if stock is insufficient or SKU not found.
# 3. Write  restock(inv, sku, qty)  – increase stock.
# 4. Write  low_stock(inv, threshold=5)  – returns a list of items
#    where stock <= threshold, sorted by stock ascending.
# 5. Pre-load 5 items, perform several sells and restocks,
#    then print the full inventory table and the low-stock alert list.


# -------------------------------------------------------------
# TASK 3 – Text Scrambler
# -------------------------------------------------------------
# A "word scramble" keeps the first and last letters of each word
# in place and shuffles the middle letters.
# e.g. "python" might become "phtyon"
# (Use a fixed seed so results are reproducible: import random; random.seed(42))
# 1. Write a function  scramble_word(word)  that scrambles the middle
#    letters of a word.  Words of length <= 3 are returned unchanged.
# 2. Write a function  scramble_sentence(sentence)  that applies
#    scramble_word to every word, preserving spaces.
# 3. Test with at least 3 sentences.
# 4. Write a function  unscramble_check(original, scrambled)  that checks
#    whether the first/last letters still match for every word.
#    Return True if the scramble is valid, False otherwise.
# 5. Run unscramble_check on your scrambled results and print the verdict.


# -------------------------------------------------------------
# TASK 4 – Simple Statistics from Scratch
# -------------------------------------------------------------
# Write all functions WITHOUT using the statistics or math modules.
# 1. Write  mean(data)  – returns the arithmetic mean.
# 2. Write  median(data)  – returns the middle value (or average of two
#    middle values) of a sorted copy of data.
# 3. Write  mode(data)  – returns the most frequent value.
#    If there's a tie, return all tied values as a sorted list.
# 4. Write  variance(data)  – returns the population variance.
#    Formula: average of squared differences from the mean.
# 5. Test all four on two datasets:
#       [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
#       [1, 1, 1, 1, 5]
#    Print a stats summary for each dataset.


# -------------------------------------------------------------
# TASK 5 – Command Parser
# -------------------------------------------------------------
# Build a simple text command parser.
# Supported commands:
#   "add <name> <score>"     → adds student with score
#   "remove <name>"          → removes student
#   "show"                   → prints all students sorted by score
#   "top <n>"                → prints top n students
#   "average"                → prints class average
#
# 1. Write a function  parse_command(command_str)  that splits the
#    string and returns a (command, args) tuple.
# 2. Write a function  run(command_str, students)  that dispatches
#    to the right action based on the parsed command.
#    Raise ValueError for unknown commands.
# 3. Handle errors gracefully: unknown name for remove, invalid score, etc.
# 4. Process this sequence of commands:
#       "add Alice 88", "add Bob 72", "add Carol 95",
#       "add Dave 60", "show", "top 2", "remove Bob",
#       "average", "show"
# 5. Print the output of each command with a "> command" header line.
