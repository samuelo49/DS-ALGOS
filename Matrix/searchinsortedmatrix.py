'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
def searchMatrix(matrix, target):
    # get number of rows
    numRows = len(matrix)
    if numRows == 0:
        return False
    
    # get number of columns
    numCols = len(matrix[0])

    # create left, right bounds for binary search
    leftPtr = 0
    rightPtr = numRows * numCols - 1

    while leftPtr <= rightPtr:
        #get midpoint index 
        pivot_idx = (leftPtr + rightPtr) // 2

        # get the pivot row and column indices
        pivot_row_index = pivot_idx // numCols 
        pivot_col_index = pivot_idx % numCols 

        # get candidate cell
        candidate_cell = matrix[pivot_row_index[pivot_col_index]]

        if target == candidate_cell:
            return True
        
        else:
            if target < candidate_cell:
                rightPtr = pivot_idx - 1

            else:
                leftPtr = pivot_idx + 1

    return False
