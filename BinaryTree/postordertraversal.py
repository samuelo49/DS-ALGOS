class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def post_order_traversal(root: Node):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)




def tree_max_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root) - 1 if root else 0





def tree_min_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        if not root.left:
            return dfs(root.right) + 1
        if not root.right:
            return dfs(root.left) + 1
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return min(dfs(root.left), dfs(root.right)) + 1
    return dfs(root)  if root else 0
