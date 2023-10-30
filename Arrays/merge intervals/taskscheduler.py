"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

"""
def leastInterval(tasks, n):
    frequencies = {}
    for t in tasks:
        frequencies[t] = frequencies.get(t, 0) + 1

    frequencies = dict(sorted(frequencies.items(), key = lambda x: x[1]))

    # get the max frequency of the most frequent task
    max_freq = frequencies.popitem()[1]

    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        # if we have more than one task with the max frequency
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time

# time complexity: O(N) where N is the number of tasks.
# space complexity: O(1) since we are using a dictionary with at most 26 keys.

# test case 1
tasks = ["A","A","A","B","B","B"]
n = 2   
print(leastInterval(tasks, n))

    