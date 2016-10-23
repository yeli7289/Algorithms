# Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
# Analysis
Similar to [Binary Tree Level Order Traversal](), use level to determine whether to reverse the sequence or not
# Code
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root,0)]
        level = 0
        ret = []
        temp = []
        while queue:
            node, l = queue.pop()
            if l > level:
                temp = temp if level%2==0 else temp[::-1]
                ret.append(temp)
                temp = [node.val]
                level = level+1
            else:
                temp.append(node.val)
            if node.left:
                queue.insert(0,(node.left,l+1))
            if node.right:
                queue.insert(0,(node.right,l+1))
                
        if level%2==0:
            ret.append(temp)
        else:
            ret.append(temp[::-1])
        return ret

```