"""
There was a bug in the Formation session tool that accidentally duplicated some Fellows in sessions.
 Given an array of names representing Fellows in a session, remove an array of all Fellows
with duplicates removed. The array must be in the same order as it appeared in the input.
Follow-up question:
If instead of creating an output array, you simply removed the Fellows in place,
what would be the impact on the runtime of the algorithm?
["oliver", "pixel", "oliver", "pinky"] => ["oliver", "pixel", "pinky"]
"""


def removeDuplicateFellows(fellows):
    return list(set(fellows))

print(removeDuplicateFellows(["oliver", "pixel", "oliver", "pinky"]))
