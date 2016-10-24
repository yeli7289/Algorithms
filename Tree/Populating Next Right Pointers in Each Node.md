# Populating Next Right Pointers in Each Node
Given a binary tree
```
struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
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
        if not root:
            return 
        queue = [root]
        while queue:
            n = queue.pop()
            if n.left:
                n.left.next = n.right
                queue.insert(0,n.left)
            if n.right:
                queue.insert(0,n.right)
                if n.next:
                    n.right.next = n.next.left
                else:
                    n.right.next = None

```