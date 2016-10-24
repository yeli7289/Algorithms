# Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?
# Analysis
Each iteration, go through all nodes in same level and connect the next level's node.
***next*** to keep track of the first node in the next layer, ***prev*** to keep track of the node to connect  
# Code
```
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            next, prev = None, None
            while root:
                if not next:
                    next = root.left if root.left else root.right
                if root.left:
                    if prev: prev.next = root.left
                    prev = root.left
                if root.right:
                    if prev: prev.next = root.right
                    prev = root.right
                root = root.next
            root = next
```