"""
Question 1: Find the Length of an Integer

Counts the digits in an integer, ignoring the minus sign.

Run:  python basics/q01_integer_length.py

Example output:
    5
"""

a = -12345
print(len(str(abs(a))))  # abs() converts negative to positive, str() for len()
