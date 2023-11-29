'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],
              [3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


🔎 EXPLORE
What are some other insightful & revealing test cases?
test1
mat = [[1,2],
       [3,4]], 
       r = 1, c = 4
 
Output: [[1,2],[3,4]] we have r = and c = 4.

test2
mat = [[1,2],
[3,4]], 
r = 2, c = 4

output = [[1,2],[3,4]]

mat = [[],[1,2]]
r = 1, c = 4
output = [[1,2]]

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
def matrixReshape(matrix,r, c):
    outer = []
    temp = []
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j])

    # if curernt number of elements doesn't equal the total number of elements for the final output then return original matrix
    if r * c != len(temp):
        return matrix
    
    # now we are sure that we have elements that can fit the structure of final result r * c

    for _ in range(r):
        # use an inner list to store elements in each row
        inner = []
        for _ in range(c):
            # fill each row based on how columns/c we have set
            #  use k as the index for each element in our temp list 
            inner.append(temp[k])

            # move to next element in the temp list 
            k +=1
        # add the current filled row to the outer list since we filled required elements based on num of columns/c
        outer.append(inner)
    return outer

# test cases
#1 
matrix_1 = [[1,2],[3,4]]
r_1 = 1 
c_1 = 4
print('test1', matrixReshape(matrix_1,r_1,c_1)) 

#2
matrix_2 = [[1,2],[3,4]]
r_2 = 2 
c_2 = 4
print('test2', matrixReshape(matrix_2,r_2,c_2)) 
