"""
Given a string and a non-empty substring sub, compute recursively the number of
times that sub appears in the string, without the substrings overlapping.
"""


def strCount(word: str, sub: str) -> int:
    if len(word) < len(sub):
        return 0
    if word[0:len(sub)] == sub:
        return 1 + strCount(word[len(sub):],sub)

    return strCount(word[1:],sub)



print(strCount("catcowcat", "cat") == 2)
print(strCount("catcowcat", "cow") == 1)
print(strCount("catcowcat", "dog") == 0)
