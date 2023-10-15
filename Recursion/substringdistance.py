"""
Given a string and a non-empty substring sub, compute recursively the size of the largest
substring which starts and ends with the given sub string and return its length,
including the length of the substrings.
When sub is multiple characters, they may overlap with each other and share characters.

print(strDist("catcowcat", "cat") == 9)
print(strDist("catcowcat", "cow") == 3)
print(strDist("cccatcowcatxx", "cat") == 9)
print(strDist("ooowhwhwooo", "whw") == 5)
"""


def strDist(word: str, sub: str) -> int:
    if len(word) < len(sub):
        return 0  # base case when the word is smaller than "sub"

    if word[0:len(sub)] == sub and word[len(word) - len(sub):] == sub:
        return len(word)  # base case when the word starts and ends with "sub"

    if not word[0:len(sub)] == sub:
        return strDist(word[1:], sub)  # remove the first character

    return strDist(word[0:len(word) - 1], sub)  # remove the last character
