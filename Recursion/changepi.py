"""
Given a string, compute recursively (no loops) a new string where all appearances
 of "pi" have been replaced by "3.14".
changePi("xpix") == "x3.14x"
changePi("pipi") == "3.143.14"
changePi("pip") == "3.14p"
"""


def changePi(word: str) -> str:
    if len(word) <= 1:
        return word

    if word[0:2] == "pi":
        return "3.14" + changePi(word[2:])

    return word[0] + changePi(word[1:])

# tests
# changePi("xpix") == "x3.14x"
# changePi("pipi") == "3.143.14"
# changePi("pip") == "3.14p"
