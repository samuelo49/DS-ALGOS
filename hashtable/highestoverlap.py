"""
Given an input dictionary mapping from the name of Fellows to
their numerical skill rating, return the skill rating with the
highest number of Fellows.
{"oliver": 3, "pixel": 1, "pinky": 3} => 3
"""


def highestSkillOverlap(fellowSkills,m):
    if len(fellowSkills.keys()) == 0:
        return None
    # maxRating = 0
    # result = []
    # for fellowSkill, rating in fellowSkills.items():
    #     maxRating = max(maxRating, rating)
    # return maxRating
    topFellows = sorted(fellowSkills, reverse=True)[0]
    return topFellows


print(highestSkillOverlap({"oliver": 3, "pixel": 1, "pinky": 3},2))
# print(highestSkillOverlap({"oliver": 3}))