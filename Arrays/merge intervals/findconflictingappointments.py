'''
Problem 1: Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.

Explore
[[2,3],[3,6],[4,5],[5,7], [7,8]]

last_end = 3
current = [3,6]
last_end = 6
current = [4,5]
conflict = {[3,6],[4,5]}
last_end = 6
current = [5,7]
[3,6],[4,5],[4,5],[5,7]
Brainstorm

plan
    - outline your solution in a human readable language
implement
    - translate your plan into code

verify
    - test code against an output of some test cases 
'''
def find_conflicts(appointments):
    if not appointments:
        return []
    appointments.sort(key=lambda x: x[0])
    conflicts = []
    last_end = appointments[0][1]

    for i in range(1,len(appointments)):
        if appointments[i][0] < last_end:
            conflicts.append((appointments[i-1],appointments[i]))
            print(f"{appointments[i]} and {appointments[i - 1]} conflict.")
        last_end = max(appointments[i][1], last_end)
print(find_conflicts([[4,5], [2,3], [3,6], [5,7], [7,8]]))