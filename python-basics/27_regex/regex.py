# =============================================================
# PYTHON RegEx (Regular Expressions)
# =============================================================

# RegEx is a sequence of characters that defines a search pattern.
# Python's re module provides full regex support.

import re

# =============================================================
# CORE FUNCTIONS
# =============================================================

text = "The rain in Spain stays mainly in the plain"

# re.search() – find FIRST match anywhere in the string
m = re.search("rain", text)
print(m)            # <re.Match object; span=(4, 8), match='rain'>
print(m.span())     # (4, 8)  – start and end index
print(m.start())    # 4
print(m.end())      # 8
print(m.group())    # rain  – the matched text

# Returns None if no match
m = re.search("xyz", text)
print(m)            # None

# re.findall() – return a LIST of all matches
hits = re.findall("ain", text)
print(hits)         # ['ain', 'ain', 'ain', 'ain']

# re.finditer() – return an iterator of match objects
for m in re.finditer(r"\bin\b", text):
    print(m.span(), m.group())

# re.match() – match ONLY at the START of the string
m = re.match("The", text)
print(m)            # match

m = re.match("rain", text)
print(m)            # None – "rain" is not at the start

# re.fullmatch() – the whole string must match
m = re.fullmatch(r"\d+", "12345")
print(m)            # match

m = re.fullmatch(r"\d+", "123abc")
print(m)            # None

# re.sub() – replace matches with a string
result = re.sub("ain", "ane", text)
print(result)       # The rane in Spane stays manely in the plane

result = re.sub("ain", "ane", text, count=2)   # replace only first 2
print(result)

# re.split() – split string at each match
parts = re.split(r"\s+", "one  two   three")
print(parts)        # ['one', 'two', 'three']

parts = re.split(",", "a,b,,c", maxsplit=2)
print(parts)        # ['a', 'b', ',c']

# =============================================================
# METACHARACTERS  (special regex symbols)
# =============================================================

# .   – any character except newline
# ^   – start of string
# $   – end of string
# *   – 0 or more repetitions
# +   – 1 or more repetitions
# ?   – 0 or 1 repetition (optional)
# {}  – exact number of repetitions
# []  – character set
# \   – escape / special sequence
# |   – OR
# ()  – group

# =============================================================
# SPECIAL SEQUENCES
# =============================================================

# \d  – digit [0-9]
# \D  – non-digit
# \w  – word character [a-zA-Z0-9_]
# \W  – non-word character
# \s  – whitespace (space, tab, newline)
# \S  – non-whitespace
# \b  – word boundary
# \B  – NOT a word boundary
# \A  – start of string
# \Z  – end of string

print(re.findall(r"\d+", "I have 3 cats and 12 dogs"))   # ['3', '12']
print(re.findall(r"\w+", "Hello, World!"))               # ['Hello', 'World']
print(re.findall(r"\bcat\b", "cat concatenate cats"))    # ['cat']
print(re.findall(r"\D+", "abc123def456"))                # ['abc', 'def']

# =============================================================
# CHARACTER SETS  [ ]
# =============================================================

print(re.findall(r"[aeiou]", "Hello World"))      # ['e', 'o', 'o']
print(re.findall(r"[^aeiou]", "Hello"))           # ['H', 'l', 'l']  – NOT vowels
print(re.findall(r"[a-z]+", "Hello World 123"))   # ['ello', 'orld']
print(re.findall(r"[A-Z][a-z]+", "Hello World"))  # ['Hello', 'World']
print(re.findall(r"[0-9]+", "abc 123 def 456"))   # ['123', '456']

# =============================================================
# QUANTIFIERS
# =============================================================

print(re.findall(r"\d{3}", "123 4567 89"))          # ['123', '456']
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345")) # ['12', '123', '1234', '1234']
print(re.findall(r"colou?r", "color colour"))        # ['color', 'colour']  – u is optional
print(re.findall(r"ab*", "a ab abb abbb"))           # ['a', 'ab', 'abb', 'abbb']
print(re.findall(r"ab+", "a ab abb abbb"))           # ['ab', 'abb', 'abbb']

# =============================================================
# GROUPS  ( )
# =============================================================

# Parentheses create a capture group
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2025-06-15")
if m:
    print(m.group())     # 2025-06-15  – entire match
    print(m.group(1))    # 2025        – group 1
    print(m.group(2))    # 06          – group 2
    print(m.group(3))    # 15          – group 3
    print(m.groups())    # ('2025', '06', '15')

# Named groups
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "2025-06-15")
if m:
    print(m.group("year"))    # 2025
    print(m.group("month"))   # 06
    print(m.groupdict())      # {'year': '2025', 'month': '06', 'day': '15'}

# Non-capturing group  (?:...)
m = re.search(r"(?:https?|ftp)://([\w.]+)", "Visit https://python.org today")
if m:
    print(m.group(1))   # python.org

# =============================================================
# FLAGS
# =============================================================

# re.IGNORECASE / re.I  – case-insensitive
print(re.findall("python", "Python PYTHON python", re.I))  # ['Python', 'PYTHON', 'python']

# re.MULTILINE / re.M  – ^ and $ match at each line start/end
text = "first line\nsecond line\nthird line"
print(re.findall(r"^\w+", text, re.M))  # ['first', 'second', 'third']

# re.DOTALL / re.S  – . matches newline too
print(re.search(r"first.+third", text, re.S).group())

# re.VERBOSE / re.X  – allow whitespace and comments in pattern
pattern = re.compile(r"""
    (\d{4})   # year
    -
    (\d{2})   # month
    -
    (\d{2})   # day
""", re.X)
print(pattern.search("2025-06-15").groups())   # ('2025', '06', '15')

# =============================================================
# COMPILED PATTERNS  re.compile()
# =============================================================

# Compile once, use many times – more efficient in loops
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

emails = ["alice@example.com", "not-an-email", "bob@domain.org", "bad@"]
for e in emails:
    if email_pattern.fullmatch(e):
        print(f"  valid:   {e}")
    else:
        print(f"  invalid: {e}")

# =============================================================
# PRACTICAL PATTERNS
# =============================================================

# --- Extract all emails from text ---
text = "Contact alice@example.com or bob@domain.org for support."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)   # ['alice@example.com', 'bob@domain.org']

# --- Validate phone number ---
def is_valid_phone(phone):
    return bool(re.fullmatch(r"\+?[0-9\s\-().]{7,15}", phone))

print(is_valid_phone("+998 90 123 45 67"))   # True
print(is_valid_phone("abc"))                  # False

# --- Extract URLs ---
text = "Visit https://python.org and http://example.com for more."
urls = re.findall(r"https?://[^\s]+", text)
print(urls)

# --- Remove extra whitespace ---
messy = "Hello    World   how   are  you"
clean = re.sub(r"\s+", " ", messy).strip()
print(clean)   # Hello World how are you

# --- Extract numbers from string ---
text = "I have 3 cats, 12 fish, and 1 dog."
numbers = [int(n) for n in re.findall(r"\d+", text)]
print(numbers)   # [3, 12, 1]
print(sum(numbers))   # 16
