"""
Question 4: Factorial

Calculates n! with a loop.

Run:  python basics/q04_factorial.py

Example input:
    5

Example output:
    120
"""

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
