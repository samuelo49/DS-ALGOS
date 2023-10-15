from collections import deque
"""
Given the root of a binary tree, return the level order
traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: root = [1]
Output: [[1]]
Input: root = []
Output: []

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root:TreeNode):
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root,])
    while queue:
        levels.append([])

        levelsLength = len(queue)

        for i in range(levelsLength):
            node = queue.popleft()

            levels[level].append(node.val)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        level += 1
    return levels

print(levelOrder([3,9,20,None,None,15,7]))
