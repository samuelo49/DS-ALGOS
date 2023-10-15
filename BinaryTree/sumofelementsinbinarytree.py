"""
Q. Given a binary tree, sum all elements in the tree.
Example:
• Given a binary tree:

                 1

                / \

               7   3

              / \

             4   5

// returns 20
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_tree(root: TreeNode) -> int:
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)


print(sum_tree(None), 0)
print(sum_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
print(sum_tree(TreeNode(1)), 1)
