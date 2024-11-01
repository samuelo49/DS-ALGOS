'''
Given a binary tree, write a serialize function that converts the tree into a string and a deserialize function 
that converts a string to a binary tree. 
You may serialize the tree into any string representation you want as long as it can be deseralized.
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return '#'
    return str(root.val) + ',' + serialize(root.left) + serialize(root.right)

def deserialize(s):
    def helper(nodes):
        val = next(nodes)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node
    nodes = iter(s.split(','))
    return helper(nodes)