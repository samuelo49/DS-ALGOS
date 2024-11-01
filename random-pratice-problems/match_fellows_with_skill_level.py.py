
'''
Match Fellows by skill level

Given an input dictionary mapping Fellows (as string names) to skill ratings, 
return true if you're able to pair up Fellows with matching skill ratings with 
no Fellows leftover.
 

EXAMPLE(S)
skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == True

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == False
 

FUNCTION SIGNATURE
function canMatchFellows(skillMap) {
def canMatchFellows(skillMap: dict) -> bool:
'''
def canMatchFellows(skillMap: dict) -> bool:
    skillTracker = set()

    for skill in skillMap.values():
        if skill not in skillTracker:
            skillTracker.add(skill)
        else:
            skillTracker.remove(skill)
    return len(skillTracker) == 0

def dailyTemperatures(T):
    stack = []
    res = [0] * len(T)
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res

# Test the function
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
