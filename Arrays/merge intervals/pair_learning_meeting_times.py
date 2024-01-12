'''
Suggest Meeting Times

You've been asked to write a function that finds all available time slots for 
scheduling a meeting between a group of people. 
The function should take as input a dictionary of schedules, where each key represents a 
person and the value is a list of busy intervals during the workday. 
The busy intervals are represented as tuples of start and end times. 
For example, the following schedule shows that Alice is busy from 8am to 10am and from 1pm to 2pm, 
while Bob is busy from 9am to 11am and from 2pm to 3pm:

schedules = {
    'Alice': [(8, 10), (13, 14)],
    'Bob': [(9, 11), (14, 15)],
}

The function should also take as input the duration of the meeting in hours, 
and should return a list of all available time slots during the workday where 
the meeting can be scheduled. A workday begins at 8am and ends at 5pm. 
A time slot is represented as a single integer that represents the 
start time of the slot in hours past midnight.

Your task is to implement the find_available_slots function that takes these inputs
and returns the list of available time slots. Be sure to consider edge cases, such
as when there are no busy intervals, when the meeting duration is longer than the workday, 
and when multiple start times are possible within a single free interval.
 

EXAMPLE(S)
schedules = {
    'Alice': [(8, 10), (13, 14)],
    'Bob': [(9, 11), (14, 15)],
}

For example, if the meeting duration is 2 hours and the workday is from 8am to 5pm, 
the available time slots for the above schedule would be [11, 15], 
since those are the only times where both Alice and Bob are available for a meeting of 2 hours.
 

FUNCTION SIGNATURE
find_available_slots(schedules: dict, duration: int) -> list:

'Alice': [(8, 10), (13, 14)],
    'Bob': [(9, 11), (14, 15)],

8 9 10 11 12 13 14 15 16 17
-----         ---
  ------         ---
# Edge cases to handle
    - is it gurranted that times will be in sorted order?
    - if no busy intervals then return start_of_day and end_of_day
    - if any endTime is greater than end of work day we ignore anything after 5pm since we don't care about that
# Plan
initialize a list of busy intervals that includes the combined schedules of all individuals
we sort the combined list to make sure that we have the start times in a sorted fashion
'''
def find_available_slots(schedules, duration):
    #combine all schedules of all individuals into a single list of busy intervals.
    busy_intervals = []
    for person_schedule in schedules.values():
        busy_intervals.extend(person_schedule)

    # sort busy intervals by start time
    busy_intervals.sort()
    # busy_intervals = [(8, 10), (13, 14), (9, 11), (14, 15)]

    # Initialize a list of availabel time slots
    available_slots = []

    # Initialize the workday start and end times
    workday_start = 8
    workday_end = 17 #5pm

    # Initialize the current start time as the workday start
    current_start = workday_start

    # Now we iterate through the sorted busy intervals to find available slots
    for interval in busy_intervals:
        start, end = interval

        # Check if there's a gap between the current_start and the start of the busy interval
        if current_start + duration <= start:
            available_slots.append(current_start)
        
        # Update the current_start to the end of the current busy interval
        current_start = end

    # Check if there's a gap between the last busy interval and the end of the workday
    if current_start + duration <= workday_end:
        available_slots.append(current_start)

    return available_slots

# Example usage:
SCHEDULES = {
    'Alice': [(8, 10), (13, 14)],
    'Bob': [(9, 11), (14, 15)],
}

MEETING_DURATION = 2
available_time_slots = find_available_slots(schedules=SCHEDULES, duration=MEETING_DURATION)

print(available_time_slots)
# Output: [11, 15]
