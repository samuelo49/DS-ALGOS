"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
Input: nums = [8,8,8,2,2,6,4,4,4,4], k = 2   {8:"3",2:"2",6:"1",4:1}
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]
"""
import heapq


def freqCount(arr, k):
    countFreq = {}
    for i in range(len(arr)):
        countFreq[arr[i]] = 1 + countFreq.get(arr[i], 0)
    minHeap = []
    for key,value in countFreq.items():
        if len(minHeap) < k:
            heapq.heappush(minHeap,(value, key))
        else:
            heapq.heappushpop(minHeap,(value, key))
    result = [key for _,key in minHeap]
    return result

    # return heapq.nsmallest(k,countFreq.keys(),key=countFreq.get)


nums = ["i","love","leetcode","i","love","coding"]
k = 2
print(freqCount(nums, k))


