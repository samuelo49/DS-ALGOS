'''
Given an array of integers nums containing n + 1 integers where each integer is 
in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Steps
1. Initialize two pointers, slow and fast, at the start of the array(index 0)
2. Enter a loop that continues until the slow and fast pointers meet.
    - Move the slow pointer one step forward
    - Move the fast pointer two steps forward
    - if the slow anf fast pointers meet, it means theres a cycle which is caused by the
        duplicate number. 
3. After finding a cycle, initialize a new pointer ptr at the start ot ehf array 
    and keep the slow pointer at the meeting point. Move ptr and slow one step at a time
    until they meet. The meeting point is the duplicate number.
'''
def findDuplicate(nums):
    slow = fast = nums[0]

    # find intersection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # find the entrance to the cycle
    slow = nums[0] # same as creating new pointer ptr
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# test cases
nums_1 = [1,3,4,2,2]
print(findDuplicate(nums=nums_1)) # 2

nums_2 = [3,1,3,4,2]
print(findDuplicate(nums=nums_2)) # 3
