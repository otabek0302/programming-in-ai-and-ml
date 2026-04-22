# =============================================================
# PYTHON STRINGS
# =============================================================

# Strings are surrounded by single or double quotes – both are identical.
print("Hello")
print('Hello')

# =============================================================
# STRING METHODS  (alphabetical)
# =============================================================

# capitalize() – first char uppercase, rest lowercase
print("hello WORLD".capitalize())          # Hello world

# casefold() – aggressive lowercase for Unicode comparisons
print("Straße".casefold())                 # strasse

# center(width, fillchar) – center string in a field
print("hi".center(10, "-"))                # ----hi----

# count(sub) – count non-overlapping occurrences
print("banana".count("a"))                 # 3

# encode(encoding) – encode to bytes
print("hello".encode("utf-8"))             # b'hello'

# endswith(suffix) – True if ends with suffix
print("report.pdf".endswith(".pdf"))       # True

# expandtabs(tabsize) – replace tabs with spaces
print("A\tB".expandtabs(4))               # A   B

# find(sub) – lowest index of substring, -1 if not found
print("hello".find("l"))                   # 2

# format(*args) – replace {} placeholders
print("Hello, {}!".format("World"))        # Hello, World!

# format_map(mapping) – format with a dict
print("Hi {name}".format_map({"name": "Alice"}))  # Hi Alice

# index(sub) – like find() but raises ValueError if missing
print("hello".index("e"))                  # 1

# isalnum() – True if all alphanumeric
print("abc123".isalnum())                  # True

# isalpha() – True if all alphabetic
print("Python".isalpha())                  # True

# isascii() – True if all ASCII
print("123".isascii())                     # True

# isdecimal() – True if all decimal digits (0-9)
print("123".isdecimal())                   # True

# isdigit() – True if all digits (includes superscripts)
print("²".isdigit())                       # True

# isidentifier() – True if valid Python identifier
print("my_var".isidentifier())             # True

# islower() – True if all cased chars are lowercase
print("hello".islower())                   # True

# isnumeric() – True if all numeric (includes fractions)
print("½".isnumeric())                     # True

# isprintable() – True if all chars are printable
print("hello\n".isprintable())             # False

# isspace() – True if all whitespace
print(" ".isspace())                       # True

# istitle() – True if titlecased
print("Hello World".istitle())             # True

# isupper() – True if all cased chars uppercase
print("HELLO".isupper())                   # True

# join(iterable) – join elements with this string as separator
print("-".join(["2024", "05", "20"]))      # 2024-05-20

# ljust(width, fillchar) – left-justify in a field
print("hi".ljust(5, "*"))                  # hi***

# lower() – all lowercase
print("PYTHON".lower())                    # python

# lstrip(chars) – remove leading chars (default: whitespace)
print("  hello".lstrip())                 # hello

# maketrans(x, y) – create translation table for translate()
print(str.maketrans("ae", "AE"))           # {97: 65, 101: 69}

# partition(sep) – split at first sep → (before, sep, after)
print("user@domain.com".partition("@"))   # ('user', '@', 'domain.com')

# removeprefix(prefix) – remove prefix if present (Python 3.9+)
print("TestFile.txt".removeprefix("Test")) # File.txt

# removesuffix(suffix) – remove suffix if present (Python 3.9+)
print("TestFile.txt".removesuffix(".txt")) # TestFile

# replace(old, new, count) – replace occurrences
print("banana".replace("a", "o", 2))      # bonona

# rfind(sub) – highest index of substring, -1 if not found
print("banana".rfind("a"))                # 5

# rindex(sub) – like rfind() but raises ValueError if missing
print("banana".rindex("n"))               # 4

# rjust(width, fillchar) – right-justify in a field
print("hi".rjust(5, "*"))                 # ***hi

# rpartition(sep) – split at last sep → (before, sep, after)
print("path/to/file".rpartition("/"))     # ('path/to', '/', 'file')

# rsplit(sep, maxsplit) – split from the right
print("a,b,c".rsplit(",", 1))             # ['a,b', 'c']

# rstrip(chars) – remove trailing chars (default: whitespace)
print("hello  ".rstrip())                 # hello

# split(sep, maxsplit) – split at separator
print("apple,banana".split(","))           # ['apple', 'banana']

# splitlines(keepends) – split at line boundaries
print("line1\nline2".splitlines())         # ['line1', 'line2']

# startswith(prefix) – True if starts with prefix
print("https://site.com".startswith("https"))  # True

# strip(chars) – remove leading and trailing chars
print("  hello  ".strip())                # hello

# swapcase() – swap case of each character
print("PyThOn".swapcase())                # pYtHoN

# title() – titlecase (first letter of each word capitalized)
print("hello world".title())              # Hello World

# translate(table) – translate using a table
print("hello".translate(str.maketrans("hl", "HL")))  # HeLLo

# upper() – all uppercase
print("python".upper())                   # PYTHON

# zfill(width) – pad with zeros on the left
print("42".zfill(5))                      # 00042
