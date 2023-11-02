"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

'''
Solution: use sliding window technique and hashmaps to find anagrams
'''
from collections import Counter
def findAnagrams(s,p):
    ns, np = len(s), len(p)

    # check for edge case where s is smaller than p
    if ns < np:
        return []

    # create a hashmap to store the frequency of each character in p
    p_count = Counter(p)

    # create a hashmap to store the frequency of each character in s
    s_count = Counter()

    # create a list to store the starting indices of anagrams
    result = []

    
    # iterate through s
    for i in range(ns):
        # add one more letter
        s_count[s[i]] += 1

        # remove one letter
        if i >= np:
            if s_count[s[i - np]] == 1:
                del s_count[s[i - np]]
            else:
                s_count[s[i - np]] -= 1

        # compare the hashmap of p and s
        if p_count == s_count:
            result.append(i - np + 1)
    return result

# test case
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))

# time complexity: O(n), we iterate through s once while comparing the hashmaps, comaprison is constant time
# space complexity: O(1), the hashmaps are constant size