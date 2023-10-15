"""
Given an org chart of a company, employee A, and employee B: figure out if employee B is a direct report to employee A.
Employee B must report directly to employee A - this occurs if Employee A is the parent node of Employee B.
Employees in our tree are represented as integer values (eg: 1).
Return true if employee A manages employee B, false if not.
"""
class Node:
  def __init__(self, val, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right


def isDirectReport(person: Node, manager: int, employee: int):
    if not person:
        return False

    if person.value == manager:
        if person.left and person.left.value == employee or person.right and person.right.value == employee:
            return True
        return False
    return isDirectReport(person.left,manager,employee) or isDirectReport(person.right,manager,employee)




#     1
#   2   3
#      4  5
#     6
ceo = Node(1,
        Node(2),
        Node(3,
          Node(4,
            Node(6)),
          Node(5)
      ))

print(isDirectReport(ceo, 1, 2) == True)
print(isDirectReport(ceo, 1, 4) == False)
print(isDirectReport(ceo, 2, 1) == False)
print(isDirectReport(ceo, 2, 3) == False)