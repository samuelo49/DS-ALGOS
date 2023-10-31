"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(s: str):
    charSet = set()
    max_string_length = 0
    leftPtr = 0
    for rightPtr in range(len(s)):
        while s[rightPtr] in charSet:
            charSet.remove(s[leftPtr])
            leftPtr += 1
        charSet.add(s[rightPtr])
        max_string_length = max(max_string_length, (rightPtr - leftPtr + 1))
    return max_string_length
    
# test
s = "abcabcbb"
print(lengthOfLongestSubstring(s=s))