"""
Given a list of meetings, represented as tuples with a start and an end time, determine the minimum number of rooms required to schedule all the meetings.

Input: meetings = [[5, 10], [2, 3]] Output: 1

Input: meetings = [[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]] Output: 2
[]

Constraints

1 <= meetings.length <= 10,000
0 <= start <= 10,000
0 <= end <= 10,000
"""
def minMeetingRooms(meetings):
    if not meetings: return 0
    meetings.sort(key= lambda x: x[0]) # sort by start time 
    #  [[1, 3], [4, 6], [5, 7], [7, 9], [9, 10]]
    roomsCount = 1

    previous = meetings[0]

    for current_meeting in meetings[1:]:
        if current_meeting[0] < previous[1]:
            roomsCount += 1
        else:
            previous = current_meeting
    return roomsCount

print(minMeetingRooms([[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]]))
print(minMeetingRooms([[5, 10], [2, 3]]))

# [9]