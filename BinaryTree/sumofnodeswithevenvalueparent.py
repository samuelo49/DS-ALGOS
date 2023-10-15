"""
❓ PROMPT
Given a binary tree, return the sum of all nodes with an even-valued parent node.

Example(s)
           6
       7       8
    2    7   1   3
result = 19 (7 + 8 + 1 + 3)

           2
       5       9
result = 14 (5 + 9)

           2
    null     null
result = 0


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
function sumNodesWithEvenParent(root) {
def sumNodesWithEvenParent(root: Node) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s)
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sumNodesWithEvenParent(root: Node):
    if not root:
        return
    totalSum = [0]

    def dfs(node,parentValue=None):
        if not node:
            return
        if parentValue and parentValue % 2 == 0:
            totalSum[0] += node.value
        dfs(node.left,node.value)
        dfs(node.right,node.value)

    dfs(root)
    return totalSum[0]


root = Node(6,
  Node(7,
     Node(2),
     Node(7)
  ),
  Node(8,
      Node(1),
      Node(3)
  )
)
print(sumNodesWithEvenParent(root))