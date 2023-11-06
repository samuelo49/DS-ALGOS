"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aca", magazine = "aab"
Output: true

solution:
1. create a hash table for the magazine string, then loop through the ransomNote string and check if each character is in the hash table
if it is then decrement the value of the character in the hash table, if it is not then return false
2
    
"""
def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    magazine_dict = {}
    for char in magazine:
        magazine_dict[char] = magazine_dict.get(char, 0) + 1

    for char in ransomNote:
        if char in magazine_dict:
            if magazine_dict[char] <= 0:
                return False
            magazine_dict[char] -= 1
        else:
            return False
    return True 

# Time Complexity: O(n), since we are iterating through the list once
# Space Complexity: O(n), since we are storing the elements in a hash table

# tests
ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))

# tests
ransomNote = "aca"
magazine = "aab"
print(canConstruct(ransomNote, magazine))