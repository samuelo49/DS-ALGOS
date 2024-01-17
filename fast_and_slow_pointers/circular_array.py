'''
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.
Example1:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

Example 2:
Input: nums = [-1,-2,-3,-4,-5,6]
Output: false
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.

Example 3:
Input: nums = [1,-1,5,1,4]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so it is not a cycle.
We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).

Plan
nums = [2, -1, 1, 2, 2]
Visualizing the iteration
===========================
slow = 0
fast = 0
1st Iteration
==============
slow moves one step
fast moves two steps

slow = i = 2, value 1

fast moves two steps remember
1st 
fast = i =2, value 1
2nd 
fast = i = 3, value 2

2nd Iteration
==============
slow moves one step
slow = i = 3, value 2

fast moves two steps
1st
fast = i = 0, value = 2
2nd
fast = i = 2, value = 1

3rd Iteration
================
slow = i = 0, value = 2

fast = i = 3, value = 2
fast = i = 0  value = 2

4th iteration
==========
slow = i = 2, value = 1

fast = i = 2, value = 1
fast = i = 3, value = 2

5th iteration
slow i = 3, value = 2
fast i = 0,value = 2
fast i = 2, value = 1

6th iteration
slow i = 0, value = 2
fast i = 3, value = 2
fast i = 0, value = 2

Steps for the Algo:
1. Initialize two pointers, slow and fast, at the start of the array
2. Enter a loop that continutes until slow and fast pointers meet.
    - Move the slow pointer one step forward based on value at current index.
    - Move the fast pointer two steps forward, each step based on the value at current index.
    - If the slow an fast pointers meet, check if the cycle is valid
3. To check if cycle is valid, ensure that every number in the cycle is either all positive
    or negative.
    - Start at the index where the slow and fast pointers met.
    - Move forward based on the value at the current index and check the sign 
        of the number at the next index
    - if the sign is different, return False for an invalid cycle.
    - if you return to the start index without finding a different sign, return True
    for valid cycle
4. if the slow anf fast pointers never meet, return False because there's no cycle.
5. if a valid cycle is found, return True


'''
def circularArrayLoop(nums):
    n = len(nums)
    slow = fast = 0
    while True:
        # move slow one step
        slow = (slow + nums[slow]) % n
        #move fast two steps 
        fast = (fast + nums[fast]) % n
        fast = (fast + nums[fast]) % n

        #check if they meet
        if slow == fast:
            break
    # check if the cycle is valid
    sign = -1 if nums[slow] < 0 else 1
    while True:
        #sign of current number
        is_current_num_negative = nums[slow] < 0

        #check the sign of the first number in cycle
        is_first_num_negative = sign < 0

        # Check the sign of the first number in the cycle
        is_first_num_negative = sign < 0 

        # If the signs are different, the cycle is not valid
        if is_current_num_negative != is_first_num_negative:
            return False

        # Move to the next number in the cycle
        slow = (slow + nums[slow]) % n

        # If we've gone through the entire cycle, it's valid
        if slow == fast:
            return True

