
'''
❓ PROMPT
In this task, we're going to apply basic 2-dimensional matrix traversals to solve some simple problems.
While working on these, look out for other patterns you may have seen previously. 
Each of these takes the row- and column-major traversals and composites them with simpler 
ideas you have almost certainly encountered in one-dimensional problems.

This task is two similar problems in one:
- First, write a function that returns the average of the smallest values in each _column_.
- Write a new version of this function that returns the average of the smallest value in each _row_.

Remember that since we represent a matrix as nested arrays (an array of arrays), many problems on a matrix can be broken down into two array patterns. This makes them easier to reason about and code. 

Example(s)
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
averageRowMinimum(matrix) == 4 (because average(5, 3) = 4)
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
averageColumnMinimum(matrix)
============================
# def averageColumnMinimum(matrix):
1. Initialize an empty array to stre the minimum values of each column  
2. Initialize a variable to store the average of the minimum values
3. iterate through the matrix values in a colum-major traversal
4. find the minimum value of each column then append it to the array
5. compute the average of the minimum values
6. return the average
 

🛠️ IMPLEMENT
function averageColumnMinimum(matrix) {
function averageRowMinimum(matrix) {

def averageColumnMinimum(matrix: list[list[int]]) -> float:
def averageRowMinimum(matrix: list[list[int]]) -> float:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
-> make sure that the matrix is not empty.
-> do we assume that all inner arrays have the same length? if not
-> make sure that the matrix is not empty.

'''

# def averageColumnMinimum(matrix):
#     if len(matrix) == 0:
#         return 0
#     result = 0
#     for col in range(len(matrix[0])):
#         tempMin = float("inf")
#         for row in range(len(matrix)):
#             tempMin = min(matrix[row][col], tempMin)
#         result += tempMin
#     averageColumnMin = result // len(matrix[0])
#     return averageColumnMin

# matrix = [
#   [32, 23, 3],
#   [23,  7, 5]
# ]

# matrix_1 = []
# print(averageColumnMinimum(matrix=matrix))
# print(averageColumnMinimum(matrix=matrix_1))

def averageRowMinimum(matrix):
    total = 0
    for row in range(len(matrix)):
        tempMin = float("inf")
        for col in range(len(matrix[0])):
            tempMin = min(tempMin, matrix[row][col])
        total += tempMin
    return total // len(matrix)

matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
print(averageRowMinimum(matrix=matrix))


def set_matrix_zeros(mat):
	rows = len(mat)
	cols = len(mat[0])
	fcol = False
	frow = False

	for i in range(rows):
		if mat[i][0] == 0:
			fcol = True

	for i in range(cols):
		if mat[0][i] == 0:
			frow = True

	for i in range(1, rows):
		for j in range(1, cols):
			if mat[i][j] == 0:
				mat[0][j] = mat[i][0] = 0

	for i in range(1, rows):
		if mat[i][0] == 0:
			for j in range(1, cols):
				mat[i][j] = 0

	for j in range(1, cols):
		if mat[0][j] == 0:
			for i in range(1, rows):
				mat[i][j] = 0

	if fcol:
		for i in range(rows):
			mat[i][0] = 0

	if frow:
		for j in range(cols):
			mat[0][j] = 0
	return mat