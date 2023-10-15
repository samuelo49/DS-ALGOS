"""
Given a string that contains exactly 1 pair of parentheses, compute recursively
a new string made of only the parentheses and their contents,
so "xyz(abc)123" yields "(abc)".

Example(s)
parenBit("xyz(abc)123") == "(abc)"
parenBit("x(hello)") == "(hello)"
parenBit("(xy)1") == "(xy)"
"""


def parenBit(word: str) -> str:
    if word[0] == "(" and word[len(word) - 1] == ")":
        return word

    if word[0] == "(":
        return parenBit(word[0:len(word) - 1])

    if word[len(word) - 1] == ')':
        return parenBit(word[1:])

    return parenBit(word[1:len(word) - 1])



