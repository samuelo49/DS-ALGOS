'''
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
from typing import List

def permutations(letters):
    def dfs(start_index, path, used, res):
        if start_index == len(letters):
            res.append(''.join(path))
            return 
        
        for i, letter in enumerate(letters):
            #skip used letters
            if used[i]:
                continue

            #add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True 
            dfs(start_index + 1, path, used, res)

            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False 
    res = []
    dfs(0, [], [False] * len(letters), res)
    return res 