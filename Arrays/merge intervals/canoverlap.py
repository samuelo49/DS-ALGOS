'''
Problem 1: Given a set of intervals, find out if any two intervals overlap.

Example:

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
'''
def can_intervals_overlap(intervals):
    if not intervals:
        return False 
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            return True 
        else:
            merged.append(current)
    return False

print(can_intervals_overlap([[1,4], [2,5], [7,9]]))
print(can_intervals_overlap([]))