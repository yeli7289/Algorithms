# Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # construct the dictionary for reference for the inorder array
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, dic)
    def helper(self, inorder, inl, inr, postorder, pl, pr, dic):
        if inl > inr or pl > pr:
            return None
        root = TreeNode(postorder[pr])
        index = dic[postorder[pr]]
        root.left = self.helper(inorder, inl, index-1, postorder, pl, pl+index-inl-1, dic)
        root.right = self.helper(inorder, index+1, inr, postorder, pr-inr+index , pr-1, dic)
        return root
```