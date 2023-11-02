"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict
def groupAnagrams(strs):
    result = defaultdict(list) #mapping the character count to list of anagrams

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        result[tuple(count)].append(word)

    return result.values()

# Time Complexity: O(NK) where N is the length of strs, and K is the maximum length of a string in strs.
# Counting each string is linear in the size of the string, and we count every string.

# Space Complexity: O(NK), the total information content stored in result.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# Answer: Use a tuple instead of a fixed size array to represent the character counts.

    
