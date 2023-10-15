"""
Iteratively
Q. Given a binary tree and a target element's value, determine if the tree contains the target using depth first search (DFS).
Examples:
• Given a binary tree:

                 3

                / \

              29   4

              /     \

             2       2

                    /

                   9

• For target: 1 // returns False
• For target: 2 // returns True
"""


class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_dfs(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    if root.value == target:
        return True
    return find_dfs(root.left, target) or find_dfs(root.right, target)




# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_dfs(None, 1), False)
print(find_dfs(tree1, 9), True)
print(find_dfs(tree1, 1), False)
print(find_dfs(tree1, 2), True)
print(find_dfs(TreeNode(1), 2), False)