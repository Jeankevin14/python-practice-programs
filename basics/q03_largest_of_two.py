"""
Question 3: Largest of Two Numbers

Reads two integers and prints the larger one.

Run:  python basics/q03_largest_of_two.py

Example input:
    12
    7

Example output:
    12 is largest
"""

a = int(input())
b = int(input())
if a > b:
    print(a, "is largest")
else:
    print(b, "is largest")
