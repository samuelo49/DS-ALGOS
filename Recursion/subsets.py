"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
def generate_subsets(nums):
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        # Include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Exclude nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result

nums = [1, 2, 3]
subsets = generate_subsets(nums)
print(subsets)