# =============================================================
# Topics: functions, lists, dictionaries, loops, error handling
# =============================================================


# -------------------------------------------------------------
# TASK 1 – All Unique Checker
# -------------------------------------------------------------
# 1. Write a function  all_unique(items)  that returns True if every
#    element in the list appears exactly once, False otherwise.
#    Do NOT convert to a set directly — use a loop.
# 2. Test with:
#       [1, 2, 3, 4, 5]       → True
#       [1, 2, 3, 2, 5]       → False
#       ["a", "b", "c"]       → True
#       []                    → True  (empty list is trivially unique)
# 3. Write a related function  count_unique(items)  that returns
#    how many elements are unique (appear exactly once).
# 4. Test count_unique with: [1, 1, 2, 3, 3, 4]  →  2  (only 2 and 4).
# 5. Combine both: print a summary "X of Y items are unique" for 3 lists.


# -------------------------------------------------------------
# TASK 2 – Longest Word Finder
# -------------------------------------------------------------
# 1. Write a function  longest_word(sentence)  that returns the
#    longest word in a sentence.
#    Strip punctuation from each word before measuring.
# 2. Handle ties: if multiple words share the max length, return
#    all of them as a sorted list.
# 3. Test with at least 3 sentences, including one with a tie.
# 4. Write a function  word_lengths(sentence)  that returns a dict
#    mapping each cleaned word to its length.
# 5. Print the words sorted by length descending, with their lengths,
#    for a sentence of your choice.


# -------------------------------------------------------------
# TASK 3 – Voting System
# -------------------------------------------------------------
# Build a simple voting system using dicts and lists.
# 1. Write  register_candidate(election, name)  – adds a candidate
#    with 0 votes. Raise ValueError if already registered.
# 2. Write  cast_vote(election, name)  – adds 1 vote to the candidate.
#    Raise ValueError if candidate not found.
# 3. Write  results(election)  – returns candidates sorted by votes
#    descending; ties broken alphabetically.
# 4. Write  winner(election)  – returns the name of the top candidate,
#    or "Tie" if two or more candidates share the highest vote count.
# 5. Simulate an election:
#       - Register 4 candidates.
#       - Cast at least 12 votes spread across candidates.
#       - Print a formatted results table and announce the winner.


# -------------------------------------------------------------
# TASK 4 – List Rotation
# -------------------------------------------------------------
# 1. Write a function  rotate_right(lst, n)  that returns a new list
#    rotated n positions to the RIGHT.
#    e.g. rotate_right([1,2,3,4,5], 2) → [4, 5, 1, 2, 3]
#    Do NOT use slicing shortcuts like lst[-n:] + lst[:-n] directly —
#    build the new list with a loop or index arithmetic.
# 2. Write  rotate_left(lst, n)  that rotates to the LEFT.
# 3. Verify: rotate_left(rotate_right(lst, n), n) == lst  for any lst, n.
# 4. Handle edge cases: n=0, n larger than len(lst), empty list.
# 5. Test with 3 different lists and rotation amounts.


# -------------------------------------------------------------
# TASK 5 – Contact Book
# -------------------------------------------------------------
# Build a mini contact book using a list of dicts.
# Each contact: {"name": str, "phone": str, "email": str}
#
# 1. Write  add_contact(book, name, phone, email)  – adds a contact.
#    Raise ValueError if a contact with the same name already exists.
# 2. Write  find_contact(book, query)  – searches by name (case-insensitive,
#    partial match allowed) and returns a list of matching contacts.
# 3. Write  delete_contact(book, name)  – removes by exact name (case-insensitive).
#    Raise ValueError if not found.
# 4. Write  display_all(book)  – prints all contacts sorted alphabetically
#    by name in a formatted table.
# 5. Demonstrate the full workflow:
#       - Add 5 contacts.
#       - Search for a partial name match and print results.
#       - Delete one contact.
#       - Display the final contact book.
