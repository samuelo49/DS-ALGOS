"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
def minWindow(s,t):
    if t == "":
        return ""

    window = {}
    required_count = {}

    # populate our dict for required characters for t as the string to lookup
    for c in t:
        required_count[c] = 1 + required_count.get(c, 0)

    for c in t:
        window[c] = 0

    current, required = 0, len(required_count)

    result, result_length = [-1,-1], float("inf")

    left = 0
    for right in range(len(s)):
        c = s[right]
        if c in t:
            window[c] = 1 + window.get(c,0)

        if c in required_count and window[c] == required_count[c]:
            current += 1

        while current == required:
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = right - left + 1
            
            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in required_count and window[s[left]] < required_count[s[left]]:
                current -= 1
            left += 1
    left, right = result

    return s[left: right+1] if result_length != float("inf") else ""


        

#test
s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s=s, t=t))