"""
Q. Given a binary tree, find the element with the largest value.
Example:
• Given a binary tree:

                 1

                / \

               7   3

              / \

             4   5

// returns 7
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_max(root: TreeNode):
    if root is None:
        return float("-inf")
    maxValue = root.value
    lChild = tree_max(root.left)
    rChild = tree_max(root.right)

    if lChild > maxValue:
        maxValue = lChild
    if rChild > maxValue:
        maxValue = rChild
    return maxValue



# Test Cases
print(tree_max(None), float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3)  # 3
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
print(tree_max(TreeNode(1)), 1)
