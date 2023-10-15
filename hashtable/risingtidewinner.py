"""
Given an array of Fellows representing nominations for a Rising Tide Award
 at Formation, return the name of the winning Fellow with the most number
of nominations
print(risingTideWinner(["oliver", "pixel", "pinky", "pixel"])
 == "pixel")
"""


def risingTideWinner(nominations):
    countWins = dict()
    highestNominations = float("-inf")
    result = []
    for currentNominee in nominations:
        if currentNominee in countWins:
            countWins[currentNominee] += 1
        else:
            countWins[currentNominee] = 1

    # {"oliver":1, "pixel":2, "pinky" : 1}
    for fellow, currentNominations in countWins.items():
        if currentNominations > highestNominations:
            highestNominations = currentNominations
            result = [fellow]
        elif currentNominations == highestNominations:
            result.append(fellow)
    return ",".join(result)

print(risingTideWinner(["oliver", "pixel", "pinky", "pixel"]))