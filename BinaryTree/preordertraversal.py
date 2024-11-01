class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 

def pre_order_traversal(root:Node):
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
    else:
        return []