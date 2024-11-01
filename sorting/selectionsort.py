"""
Q. Given an unsorted array, perform selection sort in ascending order.
Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]

Solution:
    We set a current minimum as the first element in the input array
    we then move left to right and search for the smallest element
    if we find the element then we swap the element and the first element.
    we then move the currentminimum to the next element
"""


# def selectionSort(array: [int]) -> [int]:
#     for i in range(len(array)-1):
#         minIndex = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[minIndex]:
#                 minIndex = j
#         array[i],array[minIndex] = array[minIndex],array[i]
#     return array
# # Test Cases
# print(selectionSort([]))  # []
# print(selectionSort([1]))  # [1]
# print(selectionSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# print(selectionSort([-10, 1, 3, 8, -13, 32, 9, 5]))  # [-13, -10, 1, 3, 5, 8, 9, 32]



# def generate_pascals_triangle(num_rows):
#     triangle = []
    
#     for n in range(num_rows):
#         if n == 0:
#             triangle.append([1])
#         else:
#             new_row = [1]  # Start with 1
#             previous_row = triangle[-1]  # Get the last row in the triangle
#             for i in range(1, len(previous_row)):
#                 # Adding previous_row[i-1] and previous_row[i]
#                 new_row.append(previous_row[i-1] + previous_row[i])
#             new_row.append(1)  # End with 1
#             triangle.append(new_row)
    
#     return triangle

# # Example usage:
# num_rows = 5
# triangle = generate_pascals_triangle(num_rows)
# for row in triangle:
#     print(row)


# def subsets(nums):
#     result = []

#     def dfs(index, path):
#         # Add a copy of the current path to the result
#         result.append(path[:])
#         # Explore further using DFS
#         for i in range(index, len(nums)):
#             # Add the current number to the path
#             path.append(nums[i])
#             # Recurse
#             dfs(i + 1, path)
#             # Backtrack by removing the last element
#             path.pop()

#     # Start DFS from index 0 with an empty path
#     dfs(0, [])
#     return result

# # Example usage
# nums = [1, 2]
# print(subsets(nums))