# =============================================================
# PYTHON TESTING  –  unittest & pytest
# =============================================================

# unittest – built-in framework, xUnit style.
# pytest   – third-party, simpler syntax, powerful fixtures.
#
# Install pytest:  pip install pytest pytest-cov
# Run all tests:   pytest                  (auto-discovers test_*.py)
# Run with cover:  pytest --cov=. --cov-report=term-missing

import unittest
from unittest.mock import MagicMock, patch, call
import math

# =============================================================
# CODE UNDER TEST  (normally in a separate module)
# =============================================================

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner
        self._balance = balance
        self._history: list[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._history.append(f"+{amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._history.append(f"-{amount}")

    def history(self) -> list[str]:
        return list(self._history)   # return copy (immutable pattern)


# =============================================================
# UNITTEST – BASIC STRUCTURE
# =============================================================

class TestMathFunctions(unittest.TestCase):
    """Test suite for basic math helpers."""

    # setUp / tearDown run before/after EACH test
    def setUp(self):
        self.account = BankAccount("Alice", balance=100.0)

    def tearDown(self):
        pass   # cleanup (close files, db connections, etc.)

    # --- test methods must start with "test_" ---

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message(self):
        with self.assertRaises(ValueError) as ctx:
            divide(5, 0)
        self.assertIn("zero", str(ctx.exception).lower())

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_fizzbuzz_values(self):
        cases = {
            1: "1", 3: "Fizz", 5: "Buzz", 15: "FizzBuzz", 30: "FizzBuzz"
        }
        for n, expected in cases.items():
            with self.subTest(n=n):          # subTest: each case reported separately
                self.assertEqual(fizzbuzz(n), expected)


# =============================================================
# UNITTEST – BankAccount TESTS
# =============================================================

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("Bob", balance=500.0)

    def test_initial_balance(self):
        self.assertEqual(self.acc.balance, 500.0)

    def test_deposit_increases_balance(self):
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 600.0)

    def test_deposit_negative_raises(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-50)

    def test_deposit_zero_raises(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(0)

    def test_withdraw_decreases_balance(self):
        self.acc.withdraw(200)
        self.assertEqual(self.acc.balance, 300.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as ctx:
            self.acc.withdraw(1000)
        self.assertIn("Insufficient", str(ctx.exception))

    def test_history_records_transactions(self):
        self.acc.deposit(50)
        self.acc.withdraw(30)
        self.assertEqual(self.acc.history(), ["+50", "-30"])

    def test_history_returns_copy(self):
        h = self.acc.history()
        h.append("tampered")
        self.assertEqual(self.acc.history(), [])   # original untouched


# =============================================================
# UNITTEST – ASSERTIONS REFERENCE
# =============================================================

class TestAssertions(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)

    def test_identity(self):
        x = [1, 2]
        self.assertIs(x, x)
        self.assertIsNot([1, 2], [1, 2])

    def test_none_checks(self):
        self.assertIsNone(None)
        self.assertIsNotNone(42)

    def test_boolean(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)

    def test_membership(self):
        self.assertIn(3, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])

    def test_type_check(self):
        self.assertIsInstance(3.14, float)
        self.assertNotIsInstance("hi", int)

    def test_raises(self):
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)

    def test_almost_equal(self):
        self.assertAlmostEqual(3.14159, math.pi, places=4)

    def test_sequence_equal(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertTupleEqual((1, 2), (1, 2))
        self.assertSetEqual({1, 2}, {2, 1})
        self.assertDictEqual({"a": 1}, {"a": 1})

    def test_regex(self):
        self.assertRegex("hello world", r"\bworld\b")
        self.assertNotRegex("hello", r"\d")


# =============================================================
# MOCKING  –  unittest.mock
# =============================================================

class EmailService:
    """External service we want to mock."""
    def send(self, to: str, subject: str, body: str) -> bool:
        raise RuntimeError("Real email service – not called in tests")


class UserRegistration:
    def __init__(self, email_service: EmailService):
        self._email = email_service
        self._users: list[str] = []

    def register(self, username: str, email: str) -> dict:
        if username in self._users:
            raise ValueError(f"{username} already exists")
        self._users.append(username)
        self._email.send(email, "Welcome!", f"Hi {username}, welcome!")
        return {"username": username, "email": email}


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.mock_email = MagicMock(spec=EmailService)
        self.mock_email.send.return_value = True
        self.reg = UserRegistration(self.mock_email)

    def test_register_new_user(self):
        result = self.reg.register("alice", "alice@example.com")
        self.assertEqual(result["username"], "alice")

    def test_register_sends_welcome_email(self):
        self.reg.register("bob", "bob@example.com")
        self.mock_email.send.assert_called_once_with(
            "bob@example.com", "Welcome!", "Hi bob, welcome!"
        )

    def test_register_duplicate_raises(self):
        self.reg.register("carol", "carol@example.com")
        with self.assertRaises(ValueError):
            self.reg.register("carol", "carol2@example.com")

    def test_email_not_sent_on_duplicate(self):
        self.reg.register("dave", "dave@example.com")
        try:
            self.reg.register("dave", "dave2@example.com")
        except ValueError:
            pass
        self.mock_email.send.assert_called_once()   # only once for the first

    def test_mock_call_args(self):
        self.reg.register("eve", "eve@example.com")
        args, kwargs = self.mock_email.send.call_args
        self.assertEqual(args[0], "eve@example.com")


# =============================================================
# patch()  –  replace objects in their namespace
# =============================================================

import time as _time

def slow_operation() -> float:
    start = _time.perf_counter()
    _time.sleep(0.5)   # pretend this is slow
    return _time.perf_counter() - start


class TestWithPatch(unittest.TestCase):

    @patch("time.sleep")             # patches time.sleep globally
    def test_slow_operation_fast(self, mock_sleep):
        slow_operation()
        mock_sleep.assert_called_once_with(0.5)

    @patch("time.perf_counter", side_effect=[0.0, 1.5])
    @patch("time.sleep")
    def test_slow_operation_elapsed(self, mock_sleep, mock_perf):
        elapsed = slow_operation()
        self.assertAlmostEqual(elapsed, 1.5)


# =============================================================
# setUpClass / tearDownClass  –  shared expensive setup
# =============================================================

class TestWithClassSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.shared_data = list(range(1000))   # expensive setup once

    @classmethod
    def tearDownClass(cls):
        del cls.shared_data

    def test_first_element(self):
        self.assertEqual(self.shared_data[0], 0)

    def test_last_element(self):
        self.assertEqual(self.shared_data[-1], 999)

    def test_length(self):
        self.assertEqual(len(self.shared_data), 1000)


# =============================================================
# PYTEST EXAMPLES  (shown as runnable functions)
# =============================================================
# Run with:  pytest python-advanced/15_testing/testing.py -v
#
# pytest auto-discovers:
#   - files matching  test_*.py  or  *_test.py
#   - functions/methods starting with  test_

def test_add_pytest():
    assert add(2, 3) == 5

def test_divide_pytest():
    assert divide(10, 4) == 2.5

def test_divide_zero_pytest():
    import pytest
    with pytest.raises(ValueError, match="zero"):
        divide(1, 0)

def test_palindrome_pytest():
    assert is_palindrome("racecar")
    assert not is_palindrome("python")

# --- parametrize  (run same test with multiple inputs) ---
try:
    import pytest

    @pytest.mark.parametrize("n,expected", [
        (1,  "1"),
        (3,  "Fizz"),
        (5,  "Buzz"),
        (15, "FizzBuzz"),
        (9,  "Fizz"),
        (10, "Buzz"),
        (30, "FizzBuzz"),
    ])
    def test_fizzbuzz_parametrize(n, expected):
        assert fizzbuzz(n) == expected


    # --- fixture  (reusable setup, like setUp but composable) ---

    @pytest.fixture
    def account():
        """Provide a fresh BankAccount for each test."""
        return BankAccount("Test User", balance=200.0)

    @pytest.fixture
    def funded_account(account):
        account.deposit(300)
        return account   # fixtures can depend on other fixtures


    def test_deposit_pytest(account):
        account.deposit(50)
        assert account.balance == 250.0

    def test_funded_balance(funded_account):
        assert funded_account.balance == 500.0

    def test_withdraw_too_much(account):
        with pytest.raises(ValueError, match="Insufficient"):
            account.withdraw(1000)


    # --- monkeypatch  (pytest's built-in patcher) ---

    def test_with_monkeypatch(monkeypatch):
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(EmailService, "send", mock_send)
        svc = EmailService()
        svc.send("a@b.com", "Hi", "body")
        mock_send.assert_called_once()


    # --- capsys  (capture stdout/stderr) ---

    def test_print_output(capsys):
        print("hello pytest")
        captured = capsys.readouterr()
        assert "hello pytest" in captured.out


    # --- tmp_path  (temporary directory fixture) ---

    def test_file_writing(tmp_path):
        p = tmp_path / "data.txt"
        p.write_text("hello")
        assert p.read_text() == "hello"

except ImportError:
    pass   # pytest not installed – skip pytest-specific examples


# =============================================================
# TEST COVERAGE
# =============================================================

# Run:  pytest --cov=. --cov-report=term-missing
#
# Output example:
#   Name                Stmts   Miss  Cover
#   ----------------------------------------
#   testing.py            120     15    88%
#
# Target: 80%+ coverage
# Identify untested branches with --cov-report=html (opens browser)

# =============================================================
# TESTING BEST PRACTICES
# =============================================================

print("""
Best Practice        Explanation
-------------------  --------------------------------------------------
One assert per test  Each test has ONE logical assertion (easier to debug)
Descriptive names    test_withdraw_raises_when_insufficient_funds
Arrange-Act-Assert   Setup → Action → Verify (AAA pattern)
Test the interface   Test public API, not private internals
Don't mock too much  Mocking hides bugs; use real objects when cheap
Isolated tests       Tests must not depend on each other or order
Fast tests           Unit tests < 1ms; slow tests in separate suite
Test edge cases      Empty input, zero, None, max values, boundaries
""")

# =============================================================
# RUNNING TESTS
# =============================================================

# unittest:
#   python -m unittest testing.py -v
#   python -m unittest discover -s . -p "test_*.py"
#
# pytest (recommended):
#   pytest                        # discover all
#   pytest -v                     # verbose
#   pytest -k "palindrome"        # filter by name
#   pytest -x                     # stop on first failure
#   pytest --tb=short             # shorter tracebacks
#   pytest --cov=. --cov-report=term-missing   # coverage

if __name__ == "__main__":
    unittest.main(verbosity=2)
