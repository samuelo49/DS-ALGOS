"""
❓ PROMPT
Flipping a tree means rotating it 180 degrees around its vertical axis. For example:
     1
   /   \
  2     3
 / \   / \
4  5  6   7

Becomes:
     1
   /   \
  3     2
 / \   / \
7  6  5   4

Example(s)
    5 <--- root
 10   5
flip(root)

root.val == 5
root.left.val == 5
root.right.val == 10

Verify that these are leaf nodes:
root.left.left == None
root.left.right == None
root.right.left == None
root.right.right == None


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
function flip(root) {
def flip(root: Node) -> None:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flip(root: Node) -> None:
    if not root:
        return

    temp = root.left
    root.left = root.right
    root.right = temp

    flip(root.left)
    flip(root.right)
    return root
