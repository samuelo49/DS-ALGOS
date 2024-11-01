
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


🔎 EXPLORE
What are some other insightful & revealing test cases?
nums = [1,1,1,2,2,3], k = 2
    {1:3,2:2,3:1} => [1,2]

nums = [1,3,2,1,1], k = 2
    {1:3,3:2,2:1} => [1,3] or [1,2]

nums = [1,1,1,2,2,3] k = 5
    since k > len of unique elements return []

nums = [1,2] k = 3
    return []

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
    - initialize afrequency counter as dictionary to hold freq for each num in the input list
    - Initialize a minHeap to hold k elements at the maximum
    - Loop through frequency map and at iteration add the k,v to the minHeap
        - while the len of minHeap is greater  than k >
            - pop from the minheap to maintain size k
    
    return list of the keys in the minHeap
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
from collections import heapq
def topKFrequent(nums, k):
    freqMap = {}

    for item in nums: 
        freqMap[item] = 1 + freqMap.get(item, 0)

    minHeap = []
    for key,value in freqMap.items():
        heapq.heappush(minHeap, (value, key))

        while len(minHeap) > k:
            heapq.heappop(minHeap)
    
    result = [key for value,key in minHeap]
    return result 
