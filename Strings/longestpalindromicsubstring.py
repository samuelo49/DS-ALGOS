"""
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
def longestPalindrome(s):
    result = "" # result string
    result_length = 0 # result length

    for i in range(len(s)):
        # lets handle odd length palindromes
        l, r = i , 1

        # we ultimately want to expand to the left and right while the characters are the same
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > result_length:
                # if the length of the current palindrome is greater than the result length then we update the result
                result = s[l:r+1]
                result_length = r - l + 1

            # expand to the left and right
            l -= 1
            r += 1
        
        # lets handle even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > result_length:
                # if the length of the current palindrome is greater than the result length then we update the result
                result = s[l:r+1]
                result_length = r - l + 1

            # expand to the left and right
            l -= 1
            r += 1
    return result

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Driver Code
s = "babad"
print(longestPalindrome(s))

s = "cbbd"
print(longestPalindrome(s))