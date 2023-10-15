"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s, t):
    # keyT = sorted(t)
    # keyS = sorted(s)
    #
    # if keyS == keyT:
    #     return True
    # else:
    #     return False

    countT = {}
    countS = {}
    for char in s:
        countS[char] = 1 + countS.get(char, 0)

    for char in t:
        countT[char] = 1 + countT.get(char, 0)
    return countS == countT


s = "rat"
t = "car"
print(isAnagram(s, t))
