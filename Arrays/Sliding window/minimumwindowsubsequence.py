"""
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
Example 2:

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
"""
def minWindow(s1, s2):
    size_s1 = len(s1)
    size_s2 = len(s2)
    
    index_s1 = 0
    index_s2 = 0

    min_sub_length = float("inf")
    min_sub_sequence = ""

    while index_s1 < size_s1:
        if s1[index_s1] == s2[index_s2]:
            index_s2 += 1
            if index_s2 == size_s2:
                start, end = index_s1, index_s1
                index_s2 -= 1
                while index_s2 >= 0:
                    if s1[start] == s2[index_s2]:
                        index_s2 -= 1
                    start -= 1
                start += 1
                if end - start < min_sub_length:
                    min_sub_length = end - start
                    min_sub_sequence = s1[start:end + 1]
                index_s1 = start
                index_s2 = 0
        index_s1 += 1
    return min_sub_sequence
               
# tests
s1 = "abcdebdde"
s2 = "bde"
print(minWindow(s1=s1,s2=s2))


