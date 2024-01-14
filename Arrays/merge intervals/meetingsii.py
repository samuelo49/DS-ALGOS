"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

"""
def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    roomCount = 1
    previous = intervals[0]
    for current in intervals[1:]:
        if current[0] < previous[1]:
            roomCount += 1
        else:
            previous = current
    return roomCount

# tests
print(minMeetingRooms([[0,30],[5,10],[15,20]]))
print(minMeetingRooms([[7,10],[2,4]]))