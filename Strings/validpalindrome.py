"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
def isPalindrome(s):
    leftPtr = 0
    rightPtr = len(s) - 1

    while leftPtr < rightPtr:
        while leftPtr < rightPtr and not s[leftPtr].isalnum():
            leftPtr += 1
        while leftPtr < rightPtr and not s[rightPtr].isalnum():
            rightPtr -= 1

        if s[leftPtr].lower() != s[rightPtr].lower():
            return False
        leftPtr += 1
        rightPtr -= 1
    return True

# test case
s = "A man, a plan, a canal: Panama"
s2 = "race a car"

print(isPalindrome(s))