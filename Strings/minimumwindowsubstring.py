"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
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
    
    # initialize a dictionary to store the frequency of each character in t since we constanly need to check if the window contains all the characters in t
    countT = {}

    # initialize a dictionary to store the frequency of each character in the window
    countWindow = {}

    # populate our dict for required characters for t as the string to lookup
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have = 0 # number of unique characters in the window that are in t
    need = len(countT) # number of unique characters in t

    result = [-1,-1]
    result_length = float("inf")
    l = 0
    # grow the window from the right
    for r in range(len(s)):
        c = s[r]
        countWindow[c] = 1 + countWindow.get(c, 0)
        
        # if the character is in t and the frequency of the character in the window is equal to the frequency of the character in t, then we have one more character in the window that is in t
        if c in countT and countWindow[c] == countT[c]:
            have += 1

        while have == need:
            # update our result if current window is smaller than previous result
            if (r - l + 1) < result_length:
                result = [l, r]
                result_length = r - l + 1

            # shrink the window from the left
            countWindow[s[l]] -= 1
            # if the character is in t and the frequency of the character in the window is less than the frequency of the character in t, then we have one less character in the window that is in t
            if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                have -= 1

            l += 1
    l, r = result
    return s[l: r+1] if result_length != float("inf") else ""