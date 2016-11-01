# Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

# Analysis
Think of this problem as largest subset of an array, Binary tree is just a bidirectional data structure. 

DFS traverse the tree and calculate the maximum sum path at every node (included that node). So that we can derive the maximum sum path from bottom to top! Meanwhile, use a class variable to keep track of the sum of the maximum path.

Base case: not root return 0

# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_path = -32768
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max_path
        
    def dfs(self, root):
        if root==None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        cur = max(left,0)+root.val+max(right,0)
        self.max_path = max(self.max_path, cur)
        return root.val+max(left,max(right,0))

```