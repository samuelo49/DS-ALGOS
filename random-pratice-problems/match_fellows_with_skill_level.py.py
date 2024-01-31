
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

