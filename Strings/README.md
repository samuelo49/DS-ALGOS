- A string is a sequence of characters.Many tips that apply to arrays also apply to strings.

Time complexity:
Access - 0(1)
Search - 0(n)
insert - 0(n)
Remove - 0(n)

Operations Involving another String
Find Substring -> 0(n * m) => most naive approach
Concatenating strings -> 0(n + m)
Slice -> 0(m)
split(by token) -> 0(n + m)
strip(remove leading trailing whitespaces) -> 0(n)

Things to look out for during interviews
- Ask about input character set and case sensitivity.
- clarify if characters are only limited to lower case letters

Corner Cases
- Empty string
- string with 1 or 2 characters
- string with repeated characters
- string with only distinct characters

Techniques
=============

1. Counting Characters
    If you need to count the frequency of characters in a string. The most common way of doing that is using 
    a hashmap/ dictionary. 
    Usually the time complexity is 0(1) since strings are usually lower case letters (26)

2. String of unique characters
    Use the 26-bit mask technique to indicate which lower case latin characters are inside the string.
    mask = 0
    for c in word:
        mask |= (1 << (ord(c) - ord('a')))

    - perform a & on two bitmasks if you want to check if the two strings have common characters.

3. Anagram
    A word that is the result of rearranging the letters of a word or phrase to produce a new word or phrase 
    while using the original letters only once.

    To determine if two strings are anagrams, conside the following approaches:
        - Sorting both strings should produce the same resulting string. This takes 0(n.logn) time and 0(logn) space
        - frequency count of characters will help to determine if two strings are anagrams. This takes 0(n) time
        and 0(1) space

4. Palindrome
    A palindrome is a word, phrase, number or other sequence of characters which reads the same backward as forward such "madam" or "racecar"

    Ways to determine if a string is a palindrome:
        - Reverse the string and it should be equal to itself.
        - Have two pointers at the start and the end of the string.Move the pointers inward till they meet.At 
            every point in time, the characters at both pointers should match.

    - The order of characters within the same string matters, so hash tables aren't helpful.

    
