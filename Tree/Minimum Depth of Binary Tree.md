# Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Analysis
* Recursive: Find the minimum height among the left and right sub-tree.
* Iterative: BFS to search layer by layer, when a node reach the end, return the curent height.
# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right)+1
        if root.right == None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
        # iterative
        if root == None:
            return 0
        queue = [root]
        level = 1
        cur = 1
        next = 0
        while queue:
            node = queue.pop()
            cur -= 1
            if node.left == None and node.right == None:
                return level
            if node.left:
                queue.insert(0,node.left)
                next += 1
            if node.right:
                queue.insert(0,node.right)
                next += 1
            if cur == 0:
                level += 1
                cur = next
                next = 0
            
            
                

```
