"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""


def groupAnagrams(strs):
    if len(strs) < 0:
        return [strs]
    mapAnagrams = {}
    for word in strs:
        key = ''.join(sorted(word))

        if key not  in mapAnagrams:
            mapAnagrams[key] = []
            mapAnagrams[key].append(word)
        else:
            mapAnagrams[key].append(word)
    result = []
    for values in mapAnagrams.values():
        if len(values) >= 0:
            result.append(values)
    return result

sam = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(sam))



