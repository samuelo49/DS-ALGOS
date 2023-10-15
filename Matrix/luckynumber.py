"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example Inputs and Outputs
Example 1
Input: matrix = [[3, 7, 8],
                 [9, 11, 13], 
                 [15, 16, 17]]
Output: [15]

Example 2
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]

Example 2
Input: matrix = [[7,8],[1,2]]
Output: [7]
"""
# def luckyNumbers(matrix):
#     """
#     1. Find the minimum element in each row.
#     2. Find the maximum element in each column.
#     3. Find the intersection of the two sets.
#     """
#     # minimum value for each row
#     row_mins = [min(row) for row in matrix] # 

#     # maximum value for each column
#     col_maxs = [max(col) for col in zip(*matrix)]

#     luckyNumbers = []

#     for r in range(len(matrix)):
#         for c in range(len(matrix[0])):
#             if matrix[r][c] == row_mins[r] and matrix[r][c] == col_maxs[c]:
#                 luckyNumbers.append(matrix[r][c])
#     return luckyNumbers
# print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
