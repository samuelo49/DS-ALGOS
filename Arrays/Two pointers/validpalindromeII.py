"""
Write a function that takes a string as input and checks whether it can be a valid palindrome 
by removing at most one character from it.
"""
def is_palindrome(s):
    leftPtr = 0
    rightPtr = len(s) - 1
    mis_match_count = 0
    while leftPtr <= rightPtr:
        if s[leftPtr] != s[rightPtr]:
            if mis_match_count > 1:
                return False
            mis_match_count += 1
        leftPtr += 1
        rightPtr -= 1
    return True 

word = "ABCEBA"
print(is_palindrome(word))

word2 = "RACEACAT"
print(is_palindrome(word2))