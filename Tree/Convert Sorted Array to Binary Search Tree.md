# Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Analysis
Find the medium to be root
# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        m = len(nums)/2
        node = TreeNode(nums[m])
        node.left = self.sortedArrayToBST(nums[0:m])
        node.right = self.sortedArrayToBST(nums[m+1:len(nums)])
        return node
```
