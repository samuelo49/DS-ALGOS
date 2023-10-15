"""
❓ PROMPT
Given an array, write 2 recursive functions to find the minimum and maximum element in an array. You may use the *min(a,b)* and *max(a,b)* functions to shorthand picking the minimum and maximum between 2 values.

Example(s)
findMin([12, 1234, 45, 67, 1]) == 1
findMin([10, 20, 30]) == 10
findMin([8, 6, 7, 5, 3, 7]) == 3

findMax([12, 1234, 45, 67, 1]) == 1234
findMax([10, 20, 30]) == 30
findMax([8, 6, 7, 5, 3, 7]) == 8


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function findMin(arr) {
function findMax(arr) {
def findMin(arr: list[int]) -> int:
def findMax(arr: list[int]) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).
"""


def findMin(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return min(arr[0], findMin(arr[1:n]))


print(findMin([8, 6, 7, 5, 3, 7]))


def findMax(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return max(arr[0], findMax(arr[1:n]))


findMax([10, 20, 30])