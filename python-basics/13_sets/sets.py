# =============================================================
# PYTHON SETS
# =============================================================

# Sets store multiple items in a single variable.
# Properties:
#   - Unordered      (no fixed position, no index access)
#   - Unindexed      (cannot access items by index)
#   - Unchangeable*  (cannot edit existing items)
#   - No duplicates  (duplicate values are automatically removed)
# * You CAN add or remove items, but not edit existing ones.

fruits = {"apple", "banana", "cherry"}
print(fruits)           # order may vary on each run

# Duplicates are silently ignored
dupes = {"apple", "banana", "apple", "cherry"}
print(dupes)            # {'apple', 'banana', 'cherry'}

# True and 1 are considered the same value in a set (and False / 0)
s = {True, 1, False, 0, "hello"}
print(s)    # {False, True, 'hello'}  – only one of True/1 and one of False/0

# Mixed types allowed
mixed = {1, "hello", 3.14, True}

# set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

print(len(fruits))   # 3

# =============================================================
# ACCESSING ITEMS
# =============================================================

# Cannot access by index. Loop instead.
for fruit in fruits:
    print(fruit)

# Check membership with in
print("banana" in fruits)       # True
print("grape" in fruits)        # False
print("grape" not in fruits)    # True

# =============================================================
# ADDING ITEMS
# =============================================================

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")            # add one item
print(fruits)

# update() – add items from another set (or list, tuple, dict)
fruits.update(["kiwi", "melon"])
print(fruits)

fruits.update({"grape", "mango"})
print(fruits)

# =============================================================
# REMOVING ITEMS
# =============================================================

fruits = {"apple", "banana", "cherry", "orange"}

fruits.remove("banana")     # removes "banana"; raises KeyError if not found
print(fruits)

fruits.discard("grape")     # removes "grape" if present; NO error if missing
print(fruits)

popped = fruits.pop()       # removes a RANDOM item (sets are unordered)
print(popped)
print(fruits)

fruits.clear()              # empty the set
print(fruits)               # set()

del fruits                  # delete the set variable entirely

# =============================================================
# SET OPERATIONS  (math-style: union, intersection, difference)
# =============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# --- Union: all items from both sets (no duplicates) ---
print(a | b)               # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))          # same result
print(b.union(a))          # order of sets doesn't matter

# union() accepts any iterable
print(a.union([6, 7, 8]))  # works with a list too

# --- Intersection: only items present in BOTH sets ---
print(a & b)                        # {4, 5}
print(a.intersection(b))            # {4, 5}
print(a.intersection_update(b))     # updates a in-place; returns None
a = {1, 2, 3, 4, 5}                 # restore a

# --- Difference: items in a but NOT in b ---
print(a - b)                        # {1, 2, 3}
print(a.difference(b))              # {1, 2, 3}
print(b.difference(a))              # {6, 7, 8}  – order matters here

a.difference_update(b)              # removes b's items from a in-place
print(a)                            # {1, 2, 3}
a = {1, 2, 3, 4, 5}                 # restore

# --- Symmetric difference: items in EITHER set but NOT in both ---
print(a ^ b)                            # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))        # {1, 2, 3, 6, 7, 8}
a.symmetric_difference_update(b)        # updates a in-place
print(a)                                # {1, 2, 3, 6, 7, 8}
a = {1, 2, 3, 4, 5}                     # restore

# =============================================================
# SUBSET, SUPERSET, DISJOINT
# =============================================================

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {6, 7, 8}

print(x.issubset(y))     # True  – all items of x are in y
print(y.issuperset(x))   # True  – y contains all items of x
print(x.isdisjoint(z))   # True  – x and z share no items
print(x.isdisjoint(y))   # False – x and y share items

# =============================================================
# COPYING A SET
# =============================================================

original = {"apple", "banana", "cherry"}
copy1 = original.copy()   # correct: independent copy
copy2 = set(original)     # also correct

copy1.add("mango")
print(original)    # unchanged

# =============================================================
# FROZEN SET
# =============================================================

# frozenset is an immutable version of set.
# Cannot add or remove items after creation.
# Can be used as a dictionary key (unlike regular sets).

fs = frozenset({"apple", "banana", "cherry"})
print(fs)
print(type(fs))    # <class 'frozenset'>

# fs.add("mango")  # AttributeError – frozensets are immutable
# All read-only operations still work
print("apple" in fs)
print(len(fs))

# =============================================================
# SET METHODS – QUICK REFERENCE
# =============================================================

# add(x)                   – add item x
# update(iterable)         – add multiple items
# remove(x)                – remove x; KeyError if missing
# discard(x)               – remove x; no error if missing
# pop()                    – remove and return a random item
# clear()                  – empty the set
# copy()                   – return a shallow copy
# union(s)                 – return new set with all items from both
# intersection(s)          – return new set with only common items
# difference(s)            – return new set with items not in s
# symmetric_difference(s)  – return new set with items in either, not both
# issubset(s)              – True if all items of self are in s
# issuperset(s)            – True if self contains all items of s
# isdisjoint(s)            – True if no items are shared
