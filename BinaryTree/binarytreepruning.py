"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pruneTree(root: TreeNode):
    if root is None:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)

    if root.val == 0 and not root.left and not root.right:
        return None
    else:
        return root
