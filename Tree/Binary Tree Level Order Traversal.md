# Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

# Analysis
BFS tree traversal, push level to the queue in order to keep track of the level
# Code
```
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        result = [[]]
        queue = [(root,0)]
        level = 0
        while queue:
            node, l = queue.pop()
            if l>level:
                result.append([node.val])
                level = l
            else:
                result[level].append(node.val)
            if node.left:
                queue.insert(0,(node.left,l+1))
            if node.right:
                queue.insert(0,(node.right,l+1))
        return result
```