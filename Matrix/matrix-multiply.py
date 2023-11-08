'''
❓ PROMPT
In mathematics when two matrices are multiplied, the result is a new matrix where each position (i, j) in the output is the sum of the products of the ith _row_ in the first matrix and the jth _column_ in the second. This is called the [dot product](https://www.mathsisfun.com/algebra/matrix-multiplying.html).

As a follow-up, modify your code to support matrices that are *not* square. This requires that the number of columns in the first matrix be equal to the number of rows in the second so that the row x column cross products are possible.

Example(s)
a = [
  [1, 2],
  [3, 4]
]
b = [
  [5, 6],
  [7, 8]
]
matrixMultiply(a,b) ==
[
  [19,22],
  [43,50]
]
The (0, 0) position in the result is: 1 * 5 + 2 * 7 = 19
The (0, 1) position in the result is: 1 * 6 + 2 * 8 = 22
The (1, 0) position in the result is: 3 * 5 + 4 * 7 = 43
The (1, 1) position in the result is: 3 * 6 + 4 * 8 = 50
 

🔎 EXPLORE
List your assumptions & discoveries:
- we are traversing the first array in a row-major traversal and multiplying each item in the row with an item in the colum of second matrix
- we are traversing the second array in a colum-major traversal

Insightful & revealing test cases:ß
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(m*n) -> traversing through two matrices and doing some operations at every position
Space: O(n) -> we are creating a matrix to store the final product
 

📆 PLAN
Outline of algorithm #:
1. initialize the lengths for both matrices, the lengths for both rows and columns
2. initialize the starting points in both matrices
3. use the while loop to iterate both matrices
4. iterate first matrice in row-major traversal and second matrice in column major traversal.
 

🛠️ IMPLEMENT
function matrixMultiply(a, b) {
def matrixMultiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''  
def matrixMultiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
  aRow = len(a)       # Number of rows in matrix a
  aCol = len(a[0])    # Number of columns in matrix a
  bCol = len(b[0])    # Number of columns in matrix b

  res = [[0] * bCol for _ in range(aRow)]

  for i in range(aRow):
    for j in range(bCol):
      for k in range(aCol):
        res[i][j] += a[i][k] * b[k][j]
      
  return res
# tests
a = [[]]
b = [[]]
print(matrixMultiply(a,b) == [[]] or matrixMultiply(a,b) == [[None]])

a = [[5]]
b = [[10]]
print(matrixMultiply(a,b) == [[50]])

a = [
  [1, 2],
  [3, 4]]
b = [
  [5, 6],
  [7, 8]]
print(matrixMultiply(a,b) == [
  [19,22],
  [43,50]])

a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
b = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]]
print(matrixMultiply(a,b) == [
  [300,360,420],
  [660,810,960],
  [1020,1260,1500]])

a = [[1, 2, 3]]
b = [
  [4],
  [5],
  [6]]
print(matrixMultiply(a,b) == [[32]])

a = [
  [1, 2, 3],
  [4, 5, 6]]
b = [
  [10, 20],
  [30, 40],
  [50, 60]]
print(matrixMultiply(a,b) == [
  [220,280],
  [490,640]])