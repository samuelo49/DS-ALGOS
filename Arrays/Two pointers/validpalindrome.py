"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

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

Plan
1.Initialize two pointers and move them from opposite ends.
2.The first pointer starts at the beginning of the string and moves toward the middle, while the second pointer starts at the end and moves toward the middle.
3.Compare the elements at each position to detect a nonmatching pair.
4.If both pointers reach the middle of the string without encountering a nonmatching pair, the string is a palindrome.

Time complexity: 0(N) where N is len of the string we have to explore in a linear fashion
                from both ends
Space complexity: 0(1), since we don't use extra memory to store any elements while processing


"""
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left <right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True 

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s=s))

def isPalindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]



