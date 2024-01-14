'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
[ [1,2,3]
  [4,5,6]
  [7,8,9] ] 
1,4,7 2,5
  matrix[0][len(matrix[0]) // 2]
Output: [[1,4,7],
         [2,5,8],
         [3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def transpose(matrix):
    outer = []
    for i in range(len(matrix[0])):
        inner = []
        for j in range(len(matrix)):
            inner.append(matrix[j][i])
        outer.append(inner)    
    return outer

input  = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(input))

