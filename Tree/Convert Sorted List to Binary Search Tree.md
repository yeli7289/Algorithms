# Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# Analysis
Find the medium of the list by 2 pointer method
# Code
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head or not head.next:
            return head
        return self.helper(head)
    def helper(self, start):
        if not start:
            return None
        if not start.next:
            return TreeNode(start.val)
        slow, fast = start, start
        pre = ListNode(0)
        pre.next = slow
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        Node = TreeNode(slow.val)
        Node.left = self.helper(start)
        Node.right = self.helper(slow.next)
        return Node
        
```