"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    prevEnd = intervals[0][1]
    res = 0
    for current in intervals[1:]:
        if current[0] < prevEnd:
            res += 1
            prevEnd = min(prevEnd, current[1])
        else:
            prevEnd = current[1]
    return res

# tests
intervals_1 = [[1,2],[2,3],[3,4],[1,3]]
intervals_2 = [[1,2],[1,2],[1,2]]
intervals_3 = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals_1))
print(eraseOverlapIntervals(intervals_2))
print(eraseOverlapIntervals(intervals_3))
    