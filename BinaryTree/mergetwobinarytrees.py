'''
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

🔎 EXPLORE
What are some other insightful & revealing test cases?
 - both trees are not none?, sum the values of the nodes that overlap
- if one tree is none?, use the node of the tree that is not none
🧠 BRAINSTORM
- traverse both trees in a preorder traversal manner
    while respecting the guidelines above where if both trees are not none and they nodes at that depth or level overlap then sum them up
    if one is none then use the non tree node for the new tree.

What approaches could work?
Algorithm 1:
    - use a preorder traversal on both trees which essentially is going to be O(n) 
    - new tree would be 0(n)
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def mergeTrees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1