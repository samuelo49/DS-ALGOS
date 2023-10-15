"""
Given an array of arrays representing relations  child, parent1,
and parent2 in each row, print a string representing
all children of each parent.

Input: []
Output: 'No family relations'

Input: [
  ["James", "Ben", "Lisa"],
  ["George", "Taylor", "Fred"],
  ["Jen", "Ben", "Gloria"]
]
Output:
'Ben is the parent of James, Jen'
'Lisa is the parent of James'
'Taylor is the parent of George'
'Fred is the parent of George'
'Gloria is the parent of Jen'
"""


def parentToChild(relations):
    if len(relations) == 0:
        return 'No family relations'
    parentChildren = {}
    for child,parent1,parent2 in relations:
        if parent1 not in parentChildren:
            parentChildren[parent1] = [child]
        else:
            parentChildren[parent1].append(child)

        if parent2 not in parentChildren:
            parentChildren[parent2] = [child]
        else:
            parentChildren[parent2].append(child)

    for parent,children in parentChildren.items():
        children = ",".join(children)
        print(f"{parent} is the parent of {children}")





print(parentToChild([
    ["James", "Ben", "Lisa"],
    ["George", "Taylor", "Fred"],
    ["Jen", "Ben", "Gloria"]
]))
