# Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Analysis

# Code
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        start, end = 0, len(lists)-1
        while start!=end or end>0:
            if start>=end:
                start = 0
            else:
                lists[start] = self.merge2Lists(lists[start], lists[end])
                start+=1
                end-=1
        return lists[0]
    def merge2Lists(self, list1, list2):
        ret = ListNode(0)
        temp = ret
        while list1 and list2:
            if list1.val < list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next
            ret = ret.next
        if list1:
            ret.next = list1
        if list2:
            ret.next = list2
        return temp.next
                
```