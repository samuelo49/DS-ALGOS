"""
We'll say that a "skipped pair" in a string is two instances of a char separated
by a char. So "AxA" the A's make a pair. Pair's can overlap,
so "AxAxA" contains 3 skipped pairs -- 2 for A and 1 for x.
Recursively compute the number of skipped pairs in the given string.

Example(s)
countSkippedPairs("axa") == 1
countSkippedPairs("axax") == 2
countSkippedPairs("aaa") == 1
"""


def countSkippedPairs(word: str) -> int:
    if len(word) <= 2:
        return 0
    if word[0] == word[2]:
        return 1 + countSkippedPairs(word[1:])

    return countSkippedPairs(word[1:])
