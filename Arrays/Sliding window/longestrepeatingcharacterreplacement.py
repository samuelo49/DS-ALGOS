"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

"""
def characterReplacement(s, k):
    string_length = len(s)
    max_sub_string_length = 0
    character_freq_count = {}
    most_freq_character = 0
    start = 0

    for end in range(string_length):
        if s[end] in character_freq_count:
            character_freq_count[s[end]] += 1
        else:
            character_freq_count[s[end]] = 1

        most_freq_character = max(most_freq_character, character_freq_count[s[end]])

        if end - start + 1 - most_freq_character > k:
            # we slide the window one step forward
            character_freq_count[s[start]] -= 1
            start += 1
        max_sub_string_length = max(max_sub_string_length, end - start + 1)
    return max_sub_string_length

# tests
s = "ABAB"
k = 2
print(characterReplacement(s=s,k=k))

s = "AABABBA"
k = 1
print(characterReplacement(s=s,k=k))
        


        
