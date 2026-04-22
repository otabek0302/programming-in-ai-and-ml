# =============================================================
# PYTHON CONTEXT MANAGERS
# =============================================================

# A context manager guarantees setup and teardown around a block of code.
# Used with the  with  statement.
# Python calls __enter__ on entry and __exit__ on exit (even if an error occurs).

# =============================================================
# WHY CONTEXT MANAGERS?
# =============================================================

# Without context manager (risky – file may not be closed on error):
f = open("demo.txt", "w")
f.write("hello")
f.close()

# With context manager (safe – file is ALWAYS closed):
with open("demo.txt", "w") as f:
    f.write("hello")
# f is closed here, even if an exception occurred inside the block

import os
os.remove("demo.txt")

# =============================================================
# CLASS-BASED CONTEXT MANAGER  (__enter__ / __exit__)
# =============================================================

class ManagedFile:
    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode     = mode
        self.file     = None

    def __enter__(self):
        print(f"  Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file       # value bound to  as  variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False (or None) to propagate exceptions.
        # Return True to suppress them.
        if exc_type:
            print(f"  Exception suppressed: {exc_type.__name__}: {exc_val}")
            return True        # suppress the exception
        return False


with ManagedFile("test.txt", "w") as f:
    f.write("Context manager test\n")

with ManagedFile("test.txt", "r") as f:
    print(f.read())

os.remove("test.txt")

# =============================================================
# contextlib.contextmanager  (generator-based, most convenient)
# =============================================================

from contextlib import contextmanager

@contextmanager
def managed_file(filename: str, mode: str = "r"):
    """Code before yield = __enter__. Code after yield = __exit__."""
    print(f"  Opening {filename}")
    f = open(filename, mode)
    try:
        yield f            # value bound to  as  variable
    finally:
        print(f"  Closing {filename}")
        f.close()          # always runs


with managed_file("test.txt", "w") as f:
    f.write("Generator context manager\n")

with managed_file("test.txt") as f:
    print(f.read())

os.remove("test.txt")

# =============================================================
# TIMER CONTEXT MANAGER
# =============================================================

import time

@contextmanager
def timer(label: str = ""):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        tag = f"[{label}] " if label else ""
        print(f"  {tag}Elapsed: {elapsed:.6f}s")


with timer("sum"):
    total = sum(range(1_000_000))
    print(f"  Sum = {total}")

# =============================================================
# TRANSACTION CONTEXT MANAGER  (commit / rollback pattern)
# =============================================================

class FakeDatabase:
    def __init__(self):
        self._data = {"balance": 1000}
        self._backup = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value

    @contextmanager
    def transaction(self):
        self._backup = dict(self._data)
        try:
            yield self
            print("  Transaction committed")
        except Exception as e:
            self._data = self._backup
            print(f"  Transaction rolled back: {e}")
            raise


db = FakeDatabase()

# Successful transaction
with db.transaction() as t:
    t.set("balance", t.get("balance") - 200)
print(f"Balance after withdrawal: {db.get('balance')}")   # 800

# Failed transaction – rollback
try:
    with db.transaction() as t:
        t.set("balance", t.get("balance") - 500)
        raise ValueError("Unexpected error!")
except ValueError:
    pass
print(f"Balance after failed tx: {db.get('balance')}")    # 800 (restored)

# =============================================================
# SUPPRESS EXCEPTIONS
# =============================================================

from contextlib import suppress

# Equivalent to try/except with pass
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")   # no crash

print("Suppressed FileNotFoundError silently")

# =============================================================
# REDIRECT stdout
# =============================================================

from contextlib import redirect_stdout
import io

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to buffer, not terminal")
    print("Same here")

captured = buffer.getvalue()
print(f"Captured: {captured!r}")

# =============================================================
# NESTED CONTEXT MANAGERS
# =============================================================

# Classic (multiple with blocks)
with open("a.txt", "w") as a:
    with open("b.txt", "w") as b:
        a.write("file A")
        b.write("file B")

# Modern (single with, comma-separated)
with open("a.txt", "r") as a, open("b.txt", "r") as b:
    print(a.read(), b.read())

for fname in ["a.txt", "b.txt"]:
    os.remove(fname)

# =============================================================
# ExitStack  – dynamic number of context managers
# =============================================================

from contextlib import ExitStack

filenames = ["x.txt", "y.txt", "z.txt"]

# Create files
for name in filenames:
    with open(name, "w") as f:
        f.write(name)

# Open a dynamic list of files
with ExitStack() as stack:
    files = [stack.enter_context(open(name)) for name in filenames]
    for f in files:
        print(f.read(), end=" ")
print()

for fname in filenames:
    os.remove(fname)

# =============================================================
# contextlib.closing  – use any object with a close() method
# =============================================================

from contextlib import closing

class Connection:
    def __init__(self, url: str):
        self.url = url
        print(f"  Connected to {url}")

    def query(self, sql: str) -> str:
        return f"Results of: {sql}"

    def close(self):
        print(f"  Disconnected from {self.url}")


with closing(Connection("db://localhost")) as conn:
    result = conn.query("SELECT * FROM users")
    print(result)
# close() is called automatically

# =============================================================
# REUSABLE CONTEXT MANAGER WITH contextlib.contextmanager
# =============================================================

@contextmanager
def indent(level: int = 1, char: str = "  "):
    """Print indented output inside the block."""
    prefix = char * level
    import builtins
    original_print = builtins.print

    def indented_print(*args, **kwargs):
        original_print(prefix, *args, **kwargs)

    builtins.print = indented_print
    try:
        yield
    finally:
        builtins.print = original_print


print("Normal output")
with indent(2):
    print("Indented output")
print("Normal again")
