"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
def merge(intervals):
    if not intervals:
        return []
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] > previous[-1]:
            merged.append(current)
        else:
            previous[1] = max(previous[1], current[1])
    return merged
            
# tests
intervals_1 = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals_1))