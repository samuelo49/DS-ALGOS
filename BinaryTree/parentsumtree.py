"""
Given a binary tree, modify each node value to be the sum of itself
and its parent node.
Return the root node of the modified tree.
       1
   2       4

 should turn into

      1
  3       5
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def immediateParentSum(root, parent_val=0):
    if not root:
        return 0
    immediateParentSum(root.left, root.val)

    immediateParentSum(root.right, root.val)

    root.val += parent_val
    return root
