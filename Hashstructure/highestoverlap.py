"""
Given an input dictionary mapping from the name of Fellows to their
numerical skill rating, return the skill rating with the
highest number of Fellows.
{"oliver": 3, "pixel": 1, "pinky": 3} => 3
"""


def highestSkillOverlap(fellowSkills):
    return max(val for val in fellowSkills.values())

print(highestSkillOverlap({"oliver": 3, "pixel": 1, "pinky": 3}))
