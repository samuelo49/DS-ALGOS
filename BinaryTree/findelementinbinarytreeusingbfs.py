from collections import deque
"""
Q. Given a binary tree and a target element's value, determine if the tree contains the target using breadth first search (BFS).
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


def find_bfs(root: TreeNode, target: int) -> bool:
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.value == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False


# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_bfs(None, 1), False)
print(find_bfs(tree1, 9), True)
print(find_bfs(tree1, 1), False)
print(find_bfs(tree1, 2), True)
print(find_bfs(TreeNode(1), 2), False)
