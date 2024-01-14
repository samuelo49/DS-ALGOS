"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

# sort all the letters in both strings and compare them
# sorting will take O(nlogn) time and O(1) space since the string in has n characters and 
# the alphabet has 26 characters
"""
def isAnagram(s, t):
    s_string = sorted(s)
    t_string = sorted(t)
    return s_string == t_string

# test case
# s = "anagram"
# t = "nagaram"
# s1 = "rat"
# s2 = "car"
# print(isAnagram(s, t))
# print(isAnagram(s1, s2))

# count frequency of each letter in both strings and compare them
def isAnagram2(s, t):
    s_dict = {}
    t_dict = {}

    for i in s:
        s_dict[i] = s_dict.get(i, 0) + 1

    for i in t:
        t_dict[i] = t_dict.get(i, 0) + 1

    return s_dict == t_dict
s = "anagram"
t = "nagaram"
s1 = "rat"
s2 = "car"
print(isAnagram(s, t))
print(isAnagram(s1, s2))
# time complexity: O(n) for populating the dictionaries and O(n) for comparing them