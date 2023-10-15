"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"
"""

def reverseVowels(self, s: str) -> str:
    if len(s) == 0 or not s: return s
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] not in "aeiouAEIOU":
            i += 1
        if s[j] not in "aeiouAEIOU":
            j -= 1
        if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)