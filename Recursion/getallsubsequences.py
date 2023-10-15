"""
Define a subsequence of a string s to be a list of characters from s such
that the characters appear in the same order in the list and in s.
For instance, for the string abcd, a, ab, and acd are valid subsequences,
whereas db is not, since b comes before d in the original string.
Given an input string, return all subsequences of the string except the empty string.

getAllSubsequences("abc") == [
  "a",
  "b",
  "c",
  "ab",
  "ac",
  "bc",
  "abc",
]

"""


def getAllSubsequences(word: str) -> List[str]:
    subsequences = []

    def getAllSubsequencesHelper(word, subseq, i):
        if i == len(word):
            if len(subseq) > 0:
                subsequences.append(subseq)
                return
        getAllSubsequencesHelper(word, subseq+word[i], i+1)
        getAllSubsequencesHelper(word, subseq, i + 1)

    getAllSubsequencesHelper(word, "", 0)
    return subsequences
