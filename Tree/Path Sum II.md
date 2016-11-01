# Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Analysis
DFS
# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(root, sum, ret, [])
        return ret
    def dfs(self, root, sum, ret, path):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            ret.append(path+[root.val])
            return
        self.dfs(root.left, sum-root.val, ret, path+[root.val])
        self.dfs(root.right, sum-root.val, ret, path+[root.val])
```