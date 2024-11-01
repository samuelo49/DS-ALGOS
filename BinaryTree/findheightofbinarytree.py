"""
Q. Given a binary tree, find the height of the tree.
Example:
• Given a binary tree:

                 1

                / \

               7   3

              / \

             4   5

// returns 2



"""


class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_height(root: TreeNode) -> int:
    if root is None:
        return -1
    return 1 + max(tree_height(root.left),tree_height(root.right))


# Test Cases
print(tree_height(None), -1)  # -1
print(tree_height(TreeNode(1, TreeNode(2), TreeNode(3))), 1)  # 1
print(tree_height(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3)  # 3
print(tree_height(TreeNode()), 0)  # 0

def tree_max_depth(root: TreeNode) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root) - 1 if root else 0