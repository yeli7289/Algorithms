# Balanced Binary Tree  
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


# Code
```
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) >=0
    def height(self, root):    
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height<0 or right_height<0:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        return max(left_height, right_height)+1
```