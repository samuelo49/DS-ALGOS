'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input
bst: a binary tree representing the existing BST.
p: the value of node p as described in the question
q: the value of node q as described in the question
Output
The value of the LCA between nodes p and q

Examples
Example 1:
Input:

bst = [6,2,8,0,4,7,9,x,x,3,5]
p = 2
q = 8
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p: int, q: int) -> int:
    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    else:
        return bst.val