'''
❓ PROMPT
Given a square matrix *mat*, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal *that are not part of the primary diagonal*.

Example(s)
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Element mat[1][1] = 5 is counted only once.

Input:
[[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]
Output: 8

Input: [[5]]
Output: 5
 

🔎 EXPLORE
List your assumptions & discoveries:
-> primary diagonal (top left hand all the way to bottom right hand corner)
-> second diagonal (top right hand all the way to bottom left hand corner)


Insightful & revealing test cases:
 [[1,2,3],
 [4,5,6],
 [7,8,9]]

 matrix[i][i] + matrix[i][COLS - 1 - i]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25

[[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]
Output: 8

Explanation: Diagonal sum: 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8

[[]]
output : 0
Explanation: There is no element to sum

[[2]]
output  : 2

[[2, 3]]

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function diagonalSum(matrix) {
def diagonalSum(matrix: list[list[int]]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def diagonalSum(matrix):
    if len(matrix) < 0:
        return 0
    ROWS = len(matrix) 
    COLS = len(matrix[0])
    total = 0
    for i in range(ROWS):
        # total += (matrix[i][i] + matrix[ROWS - 1 - i][i])
        total += (matrix[i][i] + matrix[i][COLS - 1 - i]) 
    if ROWS % 2 != 0:
        total = total - (matrix[COLS//2][COLS//2])
    return total

matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(matrix_1))