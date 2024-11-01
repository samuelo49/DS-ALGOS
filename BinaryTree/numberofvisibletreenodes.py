'''
In a binary tree, a node is labeled as "visible" if, on the path from the root to that node, 
there isn't any node with a value higher than this node's value.

The root is always "visible" since there are no other nodes between the root and itself. 
Given a binary tree, count the number of "visible" nodes.


                 5

                / \

               4   6

              / \

             3   8
Output: 3

For example: Node 4 is not visible since 5>4, similarly Node 3 is not visible since 
both 5>3 and 4>3. Node 8 is visible since all 5<=8, 4<=8, and 8<=8.
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs(root, max_so_far):
        if root is None:
            return 0
        
        visible_nodes_count = 0
        if root.val >= max_so_far:
            visible_nodes_count += 1
        
        visible_nodes_count += dfs(root.left, max(max_so_far, root.val))
        visible_nodes_count += dfs(root.right, max(max_so_far, root.val))

        return visible_nodes_count
    return dfs(root, -float('inf'))