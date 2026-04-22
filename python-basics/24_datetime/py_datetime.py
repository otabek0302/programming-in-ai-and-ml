# =============================================================
# PYTHON DATETIME
# =============================================================

# Python has no built-in date type – use the datetime module.
# Main classes inside datetime:
#   datetime.date      – year, month, day
#   datetime.time      – hour, minute, second, microsecond
#   datetime.datetime  – date + time combined
#   datetime.timedelta – duration / difference between two datetimes
#   datetime.timezone  – timezone info

import datetime

# =============================================================
# datetime.datetime  (most common class)
# =============================================================

# Current date and time (local)
now = datetime.datetime.now()
print(now)               # e.g. 2026-04-22 14:35:22.123456
print(type(now))         # <class 'datetime.datetime'>

# Access individual parts
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.weekday())     # 0=Monday … 6=Sunday
print(now.isoweekday())  # 1=Monday … 7=Sunday

# Current UTC time
utc_now = datetime.datetime.utcnow()
print(utc_now)

# Create a specific datetime
dt = datetime.datetime(2025, 6, 15, 9, 30, 0)
print(dt)   # 2025-06-15 09:30:00

# =============================================================
# datetime.date
# =============================================================

today = datetime.date.today()
print(today)              # e.g. 2026-04-22
print(today.year)
print(today.month)
print(today.day)

d = datetime.date(2000, 1, 1)
print(d)   # 2000-01-01

# =============================================================
# datetime.time
# =============================================================

t = datetime.time(14, 30, 45)
print(t)              # 14:30:45
print(t.hour)
print(t.minute)
print(t.second)

# =============================================================
# FORMATTING  – strftime()  (datetime → string)
# =============================================================

# strftime = "string format time"
now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d"))             # 2026-04-22
print(now.strftime("%d/%m/%Y"))             # 22/04/2026
print(now.strftime("%B %d, %Y"))            # April 22, 2026
print(now.strftime("%A"))                   # Tuesday (full weekday name)
print(now.strftime("%H:%M:%S"))             # 14:35:22
print(now.strftime("%I:%M %p"))             # 02:35 PM  (12-hour clock)
print(now.strftime("%Y-%m-%d %H:%M:%S"))    # 2026-04-22 14:35:22

# Common format codes:
# %Y  – 4-digit year        2026
# %y  – 2-digit year        26
# %m  – month (01-12)       04
# %B  – full month name     April
# %b  – short month name    Apr
# %d  – day (01-31)         22
# %A  – full weekday        Tuesday
# %a  – short weekday       Tue
# %H  – hour 24h (00-23)    14
# %I  – hour 12h (01-12)    02
# %M  – minute (00-59)      35
# %S  – second (00-59)      22
# %f  – microsecond         123456
# %p  – AM or PM            PM
# %j  – day of year (001-366) 112

# =============================================================
# PARSING  – strptime()  (string → datetime)
# =============================================================

# strptime = "string parse time"
s = "2025-12-25 08:00:00"
dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt)                # 2025-12-25 08:00:00
print(type(dt))          # <class 'datetime.datetime'>

dt2 = datetime.datetime.strptime("25 Dec 2025", "%d %b %Y")
print(dt2)               # 2025-12-25 00:00:00

# =============================================================
# timedelta  – arithmetic with dates
# =============================================================

now = datetime.datetime.now()

# Add / subtract time
one_week    = datetime.timedelta(weeks=1)
ten_days    = datetime.timedelta(days=10)
two_hours   = datetime.timedelta(hours=2)
thirty_mins = datetime.timedelta(minutes=30)

print(now + one_week)     # 7 days from now
print(now - ten_days)     # 10 days ago
print(now + two_hours)    # 2 hours from now

# Difference between two datetimes
start = datetime.datetime(2025, 1, 1)
end   = datetime.datetime(2025, 12, 31)
diff  = end - start
print(diff)              # 364 days, 0:00:00
print(diff.days)         # 364
print(diff.total_seconds())  # 31449600.0

# Days until a future date
today = datetime.date.today()
new_year = datetime.date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"Days until next New Year: {days_left}")

# =============================================================
# TIMESTAMP (Unix time)
# =============================================================

# Seconds since 1970-01-01 00:00:00 UTC
import time

ts = time.time()
print(ts)                                     # e.g. 1745328922.123

dt_from_ts = datetime.datetime.fromtimestamp(ts)
print(dt_from_ts)

ts_back = dt_from_ts.timestamp()
print(ts_back)

# =============================================================
# ISO FORMAT
# =============================================================

now = datetime.datetime.now()
print(now.isoformat())             # 2026-04-22T14:35:22.123456

# Parse ISO format
dt = datetime.datetime.fromisoformat("2025-12-25T08:00:00")
print(dt)

# =============================================================
# TIMEZONE-AWARE DATETIMES  (Python 3.2+)
# =============================================================

from datetime import timezone, timedelta

utc = timezone.utc
now_utc = datetime.datetime.now(tz=utc)
print(now_utc)   # 2026-04-22 12:35:22.123456+00:00

# Define a custom timezone (UTC+5 for Tashkent)
uz_tz = timezone(timedelta(hours=5))
now_uz = datetime.datetime.now(tz=uz_tz)
print(now_uz)    # 2026-04-22 17:35:22.123456+05:00

# Convert between timezones
now_uz_from_utc = now_utc.astimezone(uz_tz)
print(now_uz_from_utc)

# =============================================================
# PRACTICAL EXAMPLES
# =============================================================

# --- Age calculator ---
def calculate_age(birthdate: datetime.date) -> int:
    today = datetime.date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

birthday = datetime.date(2000, 3, 2)
print(f"Age: {calculate_age(birthday)}")

# --- Is it a weekend? ---
def is_weekend(d: datetime.date) -> bool:
    return d.weekday() >= 5   # 5=Saturday, 6=Sunday

print(is_weekend(datetime.date.today()))

# --- Format a duration nicely ---
def format_duration(seconds: int) -> str:
    td = datetime.timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{td.days}d {hours}h {minutes}m {secs}s"

print(format_duration(90061))   # 1d 1h 1m 1s
