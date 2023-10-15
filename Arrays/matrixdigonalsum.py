"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the
primary diagonal.

Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Element mat[1][1] = 5 is counted only once.
"""


def diagonalSum(matrix):
    sum = 0
    n = len(matrix)
    for i in range(0, n):
        sum += matrix[i][i]
        sum += matrix[i][n - 1 - i]
    if n % 2 != 0:
        sum -= matrix[n // 2][n // 2]
    return sum

print(diagonalSum([[1,2,3],
 [4,5,6],
 [7,8,9]]))

