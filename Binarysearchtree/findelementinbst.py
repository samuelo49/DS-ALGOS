"""
Q. Given a binary search tree and a target integer,
check if the tree contains a target.
Examples:
• Given a binary search tree:

                  8

                /   \

               3     10

              / \      \

             1   6      14

                       /

                     13

• For target: 4 // returns False
• For target: 14 // returns True
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def search_bst(root: TreeNode, target):
    if root is None:
        return None
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.value == target:
            return True
        if curr.left:
             stack.append(curr.left)
            
        if curr.right:
            stack.append(curr.right)
    return False



# Test Cases
tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(search_bst(None, 1), False)
print(search_bst(tree, 1), True)
print(search_bst(tree, 14), True)
print(search_bst(tree, 2), False)
print(search_bst(tree, 13), True)
