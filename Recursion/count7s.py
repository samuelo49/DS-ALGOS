"""
Given a non-negative int n, return the count of the occurrences of 7 as a digit,
so for example 717 yields 2. (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while integer division by 10 removes the rightmost digit (126 / 10 is 12).
Be aware that some languages require some special handling to do integer
division while others do not.

Example(s)
count7(7) == 1
count7(123) == 0
count7(717) == 2
"""


def count7(n: int) -> int:
    if n == 0:
        return 0

    if n % 10 == 7:
        return 1 + count7(n // 10)

    return count7(n // 10)
