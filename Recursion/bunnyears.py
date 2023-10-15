"""
We have a number of bunnies, each with two big floppy ears.
We want to compute the total number of ears across all the
bunnies recursively, without loops or multiplication.

print(bunnyEars(3) == 6)
print(bunnyEars(5) == 10)
"""


def bunnyEars(bunnies: int) -> int:
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies - 1)


print(bunnyEars(3) == 6)
print(bunnyEars(0))
