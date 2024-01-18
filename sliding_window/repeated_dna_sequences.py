'''
The DNA sequence is composed of a series of nucleotides abbreviated 
as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, 
return all the 10-letter-long sequences (substrings) that occur more than 
once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Plan
- Use a hashmap to keep track of the substring and its occurrances
- use an array to store our final result of strings that have more than one occurrance.

STEPS
1. Initialize a hashmap/dictionary to maintain the current substring and its count.
2. Initialize an array/list to store the substrings that have more than one occurrence.
3. Initialize a window of length 10 at the leftmost position of the string.
4. Loop through the input string, at each iteration.
    - Extract the current substring from the string using the window.
    - Check if current substring exist in our hashmap
        - if yes,increment count of occurrence for that substring.
            - if count is 2, add the substring to the result array.
        - if not, add it to the hashmap and set its occurrence to 1
    - slide the window one character to the right. This involves 
        removing the leftmost character of the substring and adding the 
        next character in the string to the right end of the substring.
5. continue the loop until the window reaches the right end of the string.
6. return the array
'''
def findRepeatedDnaSequences(str):
    look_up = {}
    result = []
    window_size = 10
    i = 0
    while i + window_size < len(str):
        current_substring = str[i:i + window_size]

        if current_substring not in look_up:
            look_up[current_substring] = 1
        else:   
            look_up[current_substring] += 1

        if look_up[current_substring] == 2:
            result.append(current_substring)
        i += 1
    return result
        


        