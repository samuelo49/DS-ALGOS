'''
A binary tree is considered balanced if, for every node in the tree, the difference in the height (or depth) of its left and right subtrees is at most 1.

In other words, the depth of the two subtrees for every node in the tree differ by no more than one.

The height (or depth) of a tree is defined as the number of edges on the longest path from the root node to any leaf node.

Note: An empty tree is considered balanced by definition.

In that case, given a binary tree, determine if it's balanced.

Parameter
tree: A binary tree.
Result
A boolean representing whether the tree given is balanced.
Examples
Example 1
Input:
                 1

                / \

               2   3
                     \
                      6
              / \

             4   5
              \
               7
output: true

                 1

                / \

             2     3
                      \
                       6
                     /
                    8
              / \

             4   5
              \
               7
output: false
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Returns -1 if is not a balanced binary tree. The height if it is.
def tree_height(tree):
    if tree is None:
        return 0
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1