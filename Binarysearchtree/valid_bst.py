'''
Given a binary tree, determine whether it is a binary search tree.
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def dfs(root, min_val, max_val):
        # empty nodes are always valid
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        # see notes below
        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    return dfs(root, -inf, inf) # root is always valid