'''
# You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, the only constraint stopping you from robbing 
# each of them is that adjacent houses have security systems connected and
#  it will automatically contact 
#the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
#  return the maximum amount
#of money you can rob tonight without alerting the police.

 

#Example 1:

#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
#Example 2:

#Input: nums = [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#Total amount you can rob = 2 + 9 + 1 = 12.

#Explore

#Input: nums = [1,2,3,1], output 4 Because (1 + 3) = 4  and (2 + 1) = 3 so the max is 4
#Input: nums = [1,2], output = 2 Because (2) is greater than (1)
#Input: nums = [2,7,9,3,1], output 12 Because (2 + 9 + 1 ) = 12, (7 + 3) = 10
#  so 12 is greater than 10
#Input: nums = [1], output 1 Because thats all we have


#Brainstorm

# call a recursive summation function starting with first element \
#  and summing everyother and compare it the tw

#Plan 

#implement

#Verify
'''
from typing import List

def house_robber(nums: List[int]) -> int:
    '''
    Robs houses along a street to maximize the amount of money without alerting the police.

    Args:
        nums (List[int]): The amount of money in each house.

    Returns:
        int: The maximum amount of money that can be robbed.
    '''
    if not nums:
        return 0
    if len(nums) < 2:
        return nums[0]

    def amount_collected(start, nums):
        if start >= len(nums):
            return 0
        return nums[start] + amount_collected(start + 2, nums)

    option_1 = amount_collected(0,nums)
    option_2 = amount_collected(1,nums)

    return max(option_1, option_2)

# Test case 1: Empty list
assert house_robber([]) == 0

# Test case 2: Single house
assert house_robber([10]) == 10

# Test case 3: Two houses with different amounts of money
assert house_robber([10, 20]) == 20

# Test case 4: Two houses with the same amount of money
assert house_robber([10, 10]) == 10

# Test case 5: Multiple houses with increasing amounts of money
assert house_robber([10, 20, 30, 40, 50]) == 90

# Test case 6: Multiple houses with decreasing amounts of money
assert house_robber([50, 40, 30, 20, 10]) == 90

# Test case 7: Multiple houses with random amounts of money
assert house_robber([20, 10, 30, 40, 50]) == 90

print("All test cases passed!")
