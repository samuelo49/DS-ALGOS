"""
Given an array of integers representing puzzle pieces and an integer targetSize,
return the number of arrangements whose size sums to targetSize.
An arrangement is a contiguous, non-empty sequence of pieces within an array.
[1,2,3]
i
  j

[5, 3, 1, 4]
"""


def puzzleArrangements(pieces, targetSize):
    arrangements = 0
    n = len(pieces)
    for i in range(0,n):
        for j in range(i + 1, n):
            if pieces[i] + pieces[j] == targetSize:
                arrangements += 1
            elif pieces[i] == targetSize or pieces[j] == targetSize:
                arrangements += 1
    return arrangements
print(puzzleArrangements([1,2,3], 3))