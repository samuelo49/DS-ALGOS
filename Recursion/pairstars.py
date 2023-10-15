"""
Given a string, compute recursively a new string where identical chars
that are adjacent in the original string are separated from each other by a "*".

print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
"""


def pairStars(word: str) -> str:
    if len(word) <= 1:
        return word

    if word[0] == word[1]:
        return str(word[0] + "*" + pairStars(word[1:]))

    return str(word[0] + pairStars(word[1:]))



