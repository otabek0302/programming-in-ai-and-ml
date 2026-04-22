# =============================================================
# PYTHON TUPLES
# =============================================================

# Tuples store multiple items in a single variable.
# Properties:
#   - Ordered        (items have a fixed position / index)
#   - Unchangeable   (cannot add, remove, or edit after creation)
#   - Allow duplicates

fruits = ("apple", "banana", "cherry")
print(fruits)
print(len(fruits))   # 3

# Mixed data types
mixed = (1, "hello", 3.14, True, None)

# Duplicates are allowed
dupes = ("apple", "banana", "apple", "cherry", "banana")
print(dupes)

# tuple() constructor
thislist = tuple(("apple", "banana", "cherry"))
print(thislist)

# --- One-item tuple needs a trailing comma ---
single = ("apple",)
print(type(single))    # <class 'tuple'>

not_a_tuple = ("apple")
print(type(not_a_tuple))  # <class 'str'>  – no comma = just parentheses

# =============================================================
# ACCESSING ITEMS
# =============================================================

fruits = ("apple", "banana", "cherry", "orange", "kiwi")

print(fruits[0])     # apple  – positive index
print(fruits[-1])    # kiwi   – negative index (from the end)

# Slicing [start:end]  – end index is NOT included
print(fruits[1:3])   # ('banana', 'cherry')
print(fruits[:3])    # ('apple', 'banana', 'cherry')
print(fruits[2:])    # ('cherry', 'orange', 'kiwi')
print(fruits[-3:-1]) # ('cherry', 'orange')

# Check membership
if "apple" in fruits:
    print("apple is in the tuple")

# =============================================================
# TUPLES ARE UNCHANGEABLE – but there are workarounds
# =============================================================

# You cannot do:
# fruits[0] = "mango"   # TypeError
# fruits.append("mango") # AttributeError

# Workaround 1: convert to list → edit → convert back
fruits = ("apple", "banana", "cherry")
temp = list(fruits)
temp[1] = "mango"
fruits = tuple(temp)
print(fruits)   # ('apple', 'mango', 'cherry')

# Workaround 2: concatenate tuples to "add" an item
fruits = ("apple", "banana", "cherry")
fruits += ("orange",)   # must be a tuple (note trailing comma)
print(fruits)           # ('apple', 'banana', 'cherry', 'orange')

# Workaround 3: delete and recreate to "remove" an item
fruits = ("apple", "banana", "cherry")
temp = list(fruits)
temp.remove("banana")
fruits = tuple(temp)
print(fruits)   # ('apple', 'cherry')

# =============================================================
# UNPACKING TUPLES
# =============================================================

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits     # parentheses are optional
print(green)    # apple
print(yellow)   # banana
print(red)      # cherry

# * collects remaining items into a list
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
(first, *middle, last) = fruits
print(first)    # apple
print(middle)   # ['banana', 'cherry', 'orange']
print(last)     # kiwi

(first, *rest) = fruits
print(first)    # apple
print(rest)     # ['banana', 'cherry', 'orange', 'kiwi']

# =============================================================
# LOOPING THROUGH A TUPLE
# =============================================================

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(i, fruits[i])

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# =============================================================
# JOINING TUPLES
# =============================================================

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

joined = tuple1 + tuple2
print(joined)   # ('a', 'b', 'c', 1, 2, 3)

# Multiply (repeat) a tuple
repeated = tuple1 * 3
print(repeated)  # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# =============================================================
# TUPLE METHODS
# =============================================================

nums = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(nums.count(5))   # 2  – count occurrences of 5
print(nums.index(8))   # 3  – index of first occurrence of 8
print(len(nums))       # 10 – number of items
print(min(nums))       # 1
print(max(nums))       # 8
print(sum(nums))       # 54

# =============================================================
# TUPLE vs LIST – when to use which?
# =============================================================

# Use a TUPLE when:
#   - Data should not change (coordinates, RGB values, DB records)
#   - You want faster iteration (tuples are slightly faster than lists)
#   - You need it as a dictionary key (lists are not hashable)

point = (10, 20)          # tuple as dict key works
locations = {point: "home"}
print(locations)

# Use a LIST when:
#   - Data needs to be modified (add, remove, update)
