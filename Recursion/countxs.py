"""
Given a string, compute recursively (no loops) the number of lowercase 'x' chars
in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0
"""


def countX(word: str) -> int:
    if len(word) < 1:
        return 0

    if word[0] == "x":
        return 1 + countX(word[1:])

    return countX(word[1:])
