import heapq
def kthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)

print(kthLargest([3,2,1,5,6,4], 2))

def kthSmallest(nums,k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return -heapq.heappop(heap)

print(kthSmallest([3,2,1,5,6,4], 2))