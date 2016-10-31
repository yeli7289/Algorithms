# Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.
# Analysis
Find the position of the root(first node in preorder) in the Inorder array, the left sub-array are the nodes in left tree, and the right sub-array are the nodes in the right tree.
# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # construct a dictionary for O(1) searching in inorder array
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, dic)
    def helper(self, preorder, pL, pR, inorder, iL, iR, dic):
        if pL>pR or iL>iR:
            return None
            
        rootvalue = preorder[pL]
        root = TreeNode(rootvalue)
        index = dic[rootvalue]
        root.left = self.helper(preorder, pL+1, index+pL-iL, inorder, iL, index-1, dic)
        root.right = self.helper(preorder, pL+index-iL+1, pR, inorder, index+1, iR, dic)
        return root
```