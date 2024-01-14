"""
HashStructuresI_wordAppend
Loop over the given array of strings to build a result string like this:
 when a string appears the 2nd, 4th, 6th, 8th, etc. time in the array,
append the string to the result.
Return the empty string if no string appears a 2nd time.

```python
["a", "b", "a"] → "a"

["a", "b", "a", "c", "a", "d", "a"] → "aa"

["a", "", "a"] → "a"
"""


def wordAppend(array):
    result = []
    lookup = {}
    for char in array:
        if char not in lookup:
            lookup[char] = 1
        else:
            lookup[char] += 1

        if lookup[char] % 2 == 0:
            result.append(char)

    if len(result) >= 1:
        return ''.join(result)
    else:
        return ''

print(wordAppend(["a", "b", "a", "c", "a", "d", "a"]))
print(wordAppend(["a", "", "a"]))
print(wordAppend(["a", "b", "a"]))



