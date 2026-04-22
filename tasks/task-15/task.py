# =============================================================
# Topics: string formatting, f-strings, numbers, loops, functions
# =============================================================


# -------------------------------------------------------------
# TASK 1 – Receipt Formatter
# -------------------------------------------------------------
# Given a list of items:
#   items = [("Coffee", 2, 3.50), ("Sandwich", 1, 6.99), ("Juice", 3, 2.25)]
#   (name, quantity, unit_price)
# 1. Print a formatted receipt with aligned columns:
#       Item          Qty   Unit    Total
#       ──────────────────────────────────
#       Coffee          2  $3.50   $7.00
#       Sandwich        1  $6.99   $6.99
#       Juice           3  $2.25   $6.75
# 2. Print the subtotal, tax (8%), and grand total below the table.
# 3. Write a function  add_item(receipt, name, qty, price)  that appends
#    a new tuple to the receipt list.
# 4. Add two more items using the function and reprint the receipt.
# 5. Highlight (add "  ← BEST VALUE" suffix) the item with the lowest unit price.


# -------------------------------------------------------------
# TASK 2 – Progress Bar Printer
# -------------------------------------------------------------
# 1. Write a function  progress_bar(current, total, width=30)
#    that prints a text progress bar like:
#       [████████████░░░░░░░░░░░░░░░░░░]  40%
#    Use "█" for filled and "░" for empty.
# 2. Calculate the number of filled blocks as a proportion of width.
# 3. Test it for current values: 0, 15, 30, 75, 100 out of 100.
# 4. Add a label parameter so it prints:
#       Downloading: [████░░░░░░░░░░░░░░░░░░░░░░░░░░]  15%
# 5. Raise ValueError if current > total or either is negative.


# -------------------------------------------------------------
# TASK 3 – Table Generator
# -------------------------------------------------------------
# 1. Write a function  print_table(headers, rows)  that prints a
#    formatted table with column widths based on the longest value
#    in each column (including the header).
# 2. Test with:
#       headers = ["Name", "Age", "City"]
#       rows    = [["Alice", 30, "New York"],
#                  ["Bob", 25, "London"],
#                  ["Carol", 35, "Tokyo"]]
# 3. Add a separator line between the header and data rows.
# 4. Right-align numeric columns and left-align string columns.
# 5. Add a row count at the bottom: "3 rows".


# -------------------------------------------------------------
# TASK 4 – Number Formatter
# -------------------------------------------------------------
# 1. Write a function  format_number(n)  that formats large integers
#    with comma separators:  1234567  →  "1,234,567"
#    Do NOT use f"{n:,}" — implement it manually with a loop or string ops.
# 2. Write a function  format_currency(amount, symbol="$")  that formats
#    a float as currency:  1234.5  →  "$1,234.50"
# 3. Write a function  format_percent(value, total, decimals=1)  that
#    returns a string like "42.5%" given value=42.5 and total=100.
# 4. Test all three functions with at least 4 inputs each.
# 5. Use all three functions together to print a financial summary:
#    sales figures, their percentage of a target, formatted as currency.


# -------------------------------------------------------------
# TASK 5 – String Template Report
# -------------------------------------------------------------
# 1. Define a multi-line f-string template for a student report card.
#    It must include: name, subject scores (at least 3), average, letter grade.
# 2. Write a function  generate_report(name, scores)  that fills in
#    the template and returns the formatted string.
# 3. Calculate the average and letter grade inside the function.
# 4. Generate and print reports for 3 different students.
# 5. Save all three reports into a single string separated by
#    a divider line ("=" * 40) and print the combined output.
