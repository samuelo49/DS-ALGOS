"""
We have bunnies standing in a line, numbered 1, 2, ...
The odd bunnies (1, 3, ..) have the usual 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears because
they each have a raised foot. Recursively return the number
of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

Example(s)
bunnyEarsTwist(2) == 5
bunnyEarsTwist(3) == 7
bunnyEarsTwist(5) == 12
"""


def bunnyEarsTwist(bunnies: int) -> int:
    if bunnies == 0:
        return 0

    if bunnies % 2 == 0:
        return 3 + bunnyEarsTwist(bunnies - 1)

    return 2 + bunnyEarsTwist(bunnies - 1)
