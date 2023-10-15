"""
matrix = [ [1, 2,  3,  4],
           [5, 6,  7,  8],
           [9, 10, 11, 12],
           [13,14, 15, 16]
        ]
1: move postiveDiagonally  => 4,7,10,13
"""


def negativeDiagonal(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        print(arr[i][n - 1 - i])


def positiveDiagonal(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        print(arr[n - 1 - i][i])


def positiveSlopingToRight(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        print(arr[i][i])


def negativeSlopingUpLeft(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        print(arr[n - 1 - i][n - 1 - i])


def swapX(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        arr[i][i], arr[i][n - 1 - i] = arr[i][n - 1 - i], arr[i][i]
    return arr

def addDiagonals(arr):
    m = len(arr)
    n = len(arr[0])
    total = 0
    for i in range(m):
        total += (arr[i][i] + arr[n - 1 - i][i])
        if len(m) % 2 == 1:
            total = total - (arr[n//2][n//2])
    return total

def spiralTraverse(arr):
    result = []
    startRow,endRow = 0,len(arr) - 1
    startCol,endCol = 0,len(arr[0]) - 1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol + 1):
            result.append(arr[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(arr[row][endCol])

        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break
            result.append(arr[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(arr[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


matrix = [[1,   2,   3,   4],
          [5,   6,   7,   8],
          [9,   10,  11, 12],
          [13,  14,  15, 16]]
# print(negativeDiagonal(matrix))
# print(positiveDiagonal(matrix))
# print(positiveSlopingToRight(matrix))
# print(negativeSlopingUpLeft(matrix))
# print(matrix)
# print(swapX(matrix))
# print(addDiagonals(matrix))
print(spiralTraverse(matrix))
