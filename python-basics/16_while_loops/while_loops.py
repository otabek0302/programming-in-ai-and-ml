# =============================================================
# PYTHON WHILE LOOPS
# =============================================================

# A while loop runs as long as its condition is True.
# Syntax:
#   while condition:
#       ...

# =============================================================
# BASIC WHILE LOOP
# =============================================================

i = 1
while i < 6:
    print(i)
    i += 1   # IMPORTANT: always update the variable or the loop runs forever

# =============================================================
# BREAK – exit the loop early
# =============================================================

# Stop when i equals 3, even though the condition (i < 6) is still True.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# prints: 1, 2, 3

# =============================================================
# CONTINUE – skip the rest of this iteration, jump to next
# =============================================================

# Skip 3, continue with the rest.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# prints: 1, 2, 4, 5, 6

# =============================================================
# ELSE – runs once when the condition becomes False
# =============================================================

# The else block does NOT run if the loop was stopped with break.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Loop finished normally")   # runs

# Else is skipped when break fires:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("This will NOT print")      # skipped because of break

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Countdown ---
count = 5
while count > 0:
    print(f"T-minus {count}")
    count -= 1
print("Liftoff!")

# --- Sum until limit ---
total = 0
n = 1
while total < 50:
    total += n
    n += 1
print(f"First n where sum >= 50: n={n-1}, sum={total}")

# --- Repeat until valid input (simulated) ---
valid_answers = ["yes", "no"]
answer = "maybe"                 # simulating a bad input
attempts = 0
while answer not in valid_answers:
    attempts += 1
    if attempts == 1:
        answer = "no"            # simulating a correction
print(f"Valid answer received: '{answer}' after {attempts} attempt(s)")

# --- Infinite loop with break ---
# while True is a common pattern when you need to loop until
# something happens inside the loop (e.g. a sentinel value).
numbers = [4, 7, 2, 9, -1, 3]   # -1 is the sentinel
index = 0
while True:
    val = numbers[index]
    if val == -1:
        print("Sentinel found, stopping.")
        break
    print(f"Processing: {val}")
    index += 1

# --- Nested while loops ---
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"  i={i}, j={j}")
        j += 1
    i += 1

# --- while + else with break inside nested logic ---
i = 0
found = False
targets = [10, 20, 30, 40, 50]
while i < len(targets):
    if targets[i] == 30:
        found = True
        break
    i += 1
else:
    print("30 not found")

if found:
    print(f"Found 30 at index {i}")
