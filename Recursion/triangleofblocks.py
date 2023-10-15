"""
We have a triangle made of blocks. The topmost row has 1 block,
the next row down has 2 blocks, the next row has 3 blocks,
and so on. Compute recursively (no loops or multiplication)
the total number of blocks in such a triangle with the given number of rows.
print(triangle(2) == 3)
print(triangle(3) == 6)
print(triangle(5) == 15)
"""


def triangle(rows):
    if rows <= 0:
        return 0
    return rows + triangle(rows - 1)

print(triangle(2))
