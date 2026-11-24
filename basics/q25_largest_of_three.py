"""
Question 25: Largest of Three Numbers (Without if-else)

Finds the largest of three numbers with max() instead of if-else.

Run:  python basics/q25_largest_of_three.py

Example input:
    3 11 6

Example output:
    Largest = 11
"""

a, b, c = map(int, input().split())
print("Largest =", max(a, b, c))
