# Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# Analysis
Recursively finding the left tree and right tree using an array to store the nodes of a tree.
# Code
```
from itertools import product
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.buildtree([i for i in range(1,n+1)]) if n>0 else []
    def buildtree(self, array):        
        ret = []
        for i in range(len(array)):
            left = self.buildtree(array[:i])
            right = self.buildtree(array[i+1:])
            for lefttree, righttree in product(left, right):
                root = TreeNode(array[i])
                root.left, root.right = lefttree, righttree
                ret.append(root)
        return ret or [None]
```