"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
def insert(intervals, new_interval):
    result = []
    for i in range(len(intervals)):
        #case when new interval is before the current interval
        if new_interval[1] < intervals[i][0]:
            result.append(new_interval)
            return result + intervals[i:]
        
        #case when new interval is after the current interval
        elif new_interval[0] > intervals[i][1]:
            result.append(intervals[i])

        #case when there is an overlap
        else:
            new_interval[0] = min(new_interval[0], intervals[i][0]) 
            new_interval[1] = max(new_interval[1], intervals[i][1])
    result.append(new_interval)
    return result


# tests
intervals_1 = [[1,3],[6,9]]
new_interval_1 = [2,5]
intervals_2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval_2 = [4,8]
print(insert(intervals_1, new_interval_1))
print(insert(intervals_2, new_interval_2))
        