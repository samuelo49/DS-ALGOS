"""
Given a set of characters, a minimum length, and a maximum length,
generate all strings that can be created using characters
from the set between those lengths inclusively.

This algorithm requires a large time and space complexity to
enumerate all the possibilities. You should be able to get
this to either time out or run out of memory even on rather small lengths.

Example(s)
generatePasswords(["a"], 2, 4) == [
  "aa",
  "aaa",
  "aaaa",
]

generatePasswords(["a", "b", "c"], 2, 3) == [
  "aa","aaa","aab","aac",
  "ab","aba","abb","abc",
  "ac","aca","acb","acc",
  "ba","baa","bab","bac",
  "bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc",
  "ca","caa","cab","cac",
  "cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"
]

"""


def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
    passwords = []
    letters = []

    def permute():
        if len(letters) > maxLength:
            return  # base case

        if minLength <= len(letters) <= maxLength:
            passwords.append(''.join(letters))

        for i in range(len(validCharacters)):
            letters.append(validCharacters[i])  # append
            permute()
            letters.pop()  # undo after recursion

    permute()

    return passwords
