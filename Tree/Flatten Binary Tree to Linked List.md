# Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.
# Code
```
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                leftnode = root.left
                while leftnode.right:
                    leftnode = leftnode.right
                leftnode.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
            else:
                root = root.right
```