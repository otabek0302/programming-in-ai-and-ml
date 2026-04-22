# =============================================================
# PYTHON LISTS
# =============================================================

# Lists store multiple items in a single variable.
# Properties:
#   - Ordered       (items have a fixed position / index)
#   - Changeable    (you can add, remove, or edit items)
#   - Allow duplicates (same value can appear multiple times)
#   - Items can be different data types

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(len(fruits))   # 3

# Mixed data types in one list
mixed = [1, "hello", 3.14, True, None]

# Duplicates are allowed
dupes = ["apple", "banana", "apple", "cherry", "banana"]
print(dupes)   # all five items kept

# list() constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# =============================================================
# ACCESSING ITEMS
# =============================================================

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print(fruits[0])    # apple   – first item (index starts at 0)
print(fruits[1])    # banana
print(fruits[-1])   # kiwi    – last item
print(fruits[-2])   # orange  – second from last

# Slicing [start:end]  – end index is NOT included
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:3])    # ['apple', 'banana', 'cherry']  – from beginning
print(fruits[2:])    # ['cherry', 'orange', 'kiwi']   – to the end
print(fruits[-3:-1]) # ['cherry', 'orange']            – negative slice

# Check if item exists
if "apple" in fruits:
    print("apple is in the list")

# =============================================================
# CHANGING ITEMS
# =============================================================

fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"          # change one item
print(fruits)                # ['apple', 'mango', 'cherry']

fruits[1:3] = ["kiwi", "melon"]  # change a range
print(fruits)                # ['apple', 'kiwi', 'melon']

# Replace a range with fewer items (list shrinks)
fruits[1:3] = ["watermelon"]
print(fruits)                # ['apple', 'watermelon']

# Replace one item with more items (list grows)
fruits[1:2] = ["kiwi", "orange"]
print(fruits)                # ['apple', 'kiwi', 'orange']

# =============================================================
# ADDING ITEMS
# =============================================================

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")       # add to the end
print(fruits)

fruits.insert(1, "mango")     # insert at index 1
print(fruits)

# extend() – add items from another list (or any iterable)
fruits.extend(["kiwi", "melon"])
print(fruits)

# extend() also works with tuples, sets, and dicts (adds keys)
fruits.extend(("pineapple", "papaya"))
print(fruits)

# =============================================================
# REMOVING ITEMS
# =============================================================

fruits = ["apple", "banana", "cherry", "banana", "orange"]

fruits.remove("banana")    # removes FIRST occurrence
print(fruits)

fruits.pop(1)              # remove by index, returns the removed item
print(fruits)

fruits.pop()               # remove last item (no index given)
print(fruits)

del fruits[0]              # delete by index
print(fruits)

fruits = ["apple", "banana", "cherry"]
del fruits                 # delete the entire list variable
# print(fruits)            # NameError – list no longer exists

fruits = ["apple", "banana", "cherry"]
fruits.clear()             # empty the list, variable still exists
print(fruits)              # []

# =============================================================
# LOOPING THROUGH A LIST
# =============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Loop using index with range()
for i in range(len(fruits)):
    print(fruits[i])

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# List comprehension (short loop to create a new list)
lengths = [len(fruit) for fruit in fruits]
print(lengths)   # [5, 6, 6]

# =============================================================
# LIST COMPREHENSION
# =============================================================

# Syntax: [expression for item in iterable if condition]

# Without comprehension:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# With comprehension:
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With condition – only even numbers:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]

# With condition on the expression:
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)    # ['even', 'odd', 'even', 'odd', 'even']

# =============================================================
# SORTING
# =============================================================

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()                  # sorts in-place, ascending (alphabetical)
print(fruits)

fruits.sort(reverse=True)      # descending
print(fruits)

numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)                 # [23, 50, 65, 82, 100]

# sort() is case-sensitive: uppercase letters come before lowercase.
mixed_case = ["banana", "Orange", "Kiwi", "cherry"]
mixed_case.sort()
print(mixed_case)              # ['Kiwi', 'Orange', 'banana', 'cherry']

# Case-insensitive sort using key parameter
mixed_case.sort(key=str.lower)
print(mixed_case)

# Custom sort with a key function
numbers = [100, 50, 65, 82, 23]
numbers.sort(key=lambda x: x % 10)  # sort by last digit
print(numbers)

# sorted() – returns a NEW sorted list, original unchanged
original = ["banana", "apple", "cherry"]
new_list = sorted(original)
print(original)   # unchanged
print(new_list)   # sorted

# reverse() – reverse the order in-place (not sorting)
fruits = ["banana", "orange", "kiwi", "cherry"]
fruits.reverse()
print(fruits)

# =============================================================
# COPYING A LIST
# =============================================================

fruits = ["apple", "banana", "cherry"]

# WRONG: this just creates another reference to the same list
ref = fruits
ref[0] = "mango"
print(fruits)     # ['mango', 'banana', 'cherry'] – original changed!

# CORRECT – copy()
fruits = ["apple", "banana", "cherry"]
copy1 = fruits.copy()
copy1[0] = "mango"
print(fruits)     # ['apple', 'banana', 'cherry'] – original safe

# CORRECT – list() constructor
copy2 = list(fruits)

# CORRECT – slice
copy3 = fruits[:]

# =============================================================
# JOINING LISTS
# =============================================================

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

joined = list1 + list2          # + creates a new list
print(joined)

list1 += list2                  # += modifies list1 in-place
print(list1)

list1.extend(list2)             # extend() appends all items from list2
print(list1)

# =============================================================
# LIST METHODS – QUICK REFERENCE
# =============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nums))           # 8   – number of items
print(nums.count(1))       # 2   – count occurrences of 1
print(nums.index(5))       # 4   – index of first occurrence of 5
print(min(nums))           # 1   – smallest value
print(max(nums))           # 9   – largest value
print(sum(nums))           # 31  – sum of all values

nums.append(7)             # add 7 at the end
nums.insert(0, 0)          # insert 0 at index 0
nums.remove(1)             # remove first occurrence of 1
popped = nums.pop()        # remove and return last item
nums.sort()                # sort in-place
nums.reverse()             # reverse in-place
nums.clear()               # empty the list
print(nums)                # []
