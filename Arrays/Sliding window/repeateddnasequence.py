"""
Given a string, s, that represents a DNA subsequence, and a number return all the contiguous subsequences (substrings) of length 
that occur more than once in the string. The order of the returned subsequences does not matter. 
If no repeated substring is found, the function should return an empty set.

The DNA sequence is composed of a series of nucleotides abbreviated as and 
For example, ACGAATTCCG is a DNA sequence. When studying DNA, it is useful to identify repeated sequences in it.
Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


"""
def findRepeatedDnaSequences(s):
    n = len(s)
    k = 10
    seen = set()
    output = set()

    for start in range(n - k + 1):
        sequence = s[start:start + k]
        if sequence in seen:
            output.add(sequence[:])
        seen.add(sequence[:])
    return output

# tests
seq = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
k = 10
print(findRepeatedDnaSequences(s=seq))

