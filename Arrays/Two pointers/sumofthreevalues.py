"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j,
i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Steps
1. Sort the input list nums in ascending order. This is necessary for the two-pointer technique used later.

2. Initialize an empty list triplets to store the triplets that sum up to the target value.

3. Start a loop over the elements of nums with the index i. This loop will consider each element as the first element of a potential triplet. The loop stops at len(nums) - 2 to leave room for the other two elements of the triplet.

4. Inside the loop, if the current element is the same as the previous one (and it's not the first element), skip this iteration to avoid adding duplicate triplets.

5. Set leftPtr to i + 1 and rightPtr to len(nums) - 1. These pointers will be used to find the other two elements of the triplet.

6. Start a while loop that continues as long as leftPtr is less than rightPtr.

7. Inside the while loop, calculate the sum of the elements at i, leftPtr, and rightPtr.

8.If the sum is greater than the target, decrement rightPtr to reduce the sum.

9.If the sum is less than the target, increment leftPtr to increase the sum.

10.If the sum is equal to the target, append the triplet to triplets, increment leftPtr, and skip any duplicate elements to avoid adding duplicate triplets.

11. After the loops finish, return the triplets list, which now contains all unique triplets in nums that sum up to the target value.

Time complexity : 0(N^2) worst case since we had to sort in place, N is the length of input array
Space Complexity: 0(N) to store the triplets
"""
def threeSum(nums, target):
    nums.sort() # sorting the array in place costs 0(nlogn)
    triplets =  []

    for i in range(len(nums) - 2): # this whole loop is 0(n * n)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        leftPtr = i + 1
        rightPtr = len(nums) - 1

        while leftPtr < rightPtr: # we are running twoSum using leftPtr and rightPtr
            threeSum = nums[i] + nums[leftPtr] + nums[rightPtr]
            if threeSum > target:
                rightPtr -= 1
            elif threeSum < target:
                leftPtr += 1
            else:
                triplets.append([nums[i],nums[leftPtr], nums[rightPtr]])
                leftPtr += 1
                while  leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr - 1]:
                    leftPtr += 1
    return triplets

# tests
nums1 = [-1,0,1,2,-1,-4]
target_1 = 0
print(threeSum(nums1, target=target_1)) 

nums2 = [0,1,1]
print(threeSum(nums2,target_1)) ==  []

