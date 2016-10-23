class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
def sortlist(head):
	# recursion base case
	if not head or not head.next:
		return head

	slow, fast = head, head.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	fast = slow.next
	slow.next = None
	L = sortlist(head)
	R = sortlist(fast)
	return merge(L, R)

def merge(left, right):
	p=ListNode(0)
	ans = p
	while left and right:
		if left.val<right.val:
			p.next = left
			left = left.next
		else:
			p.next = right
			right = right.next
		p = p.next
	if left:
		p.next = left
	if right:
		p.next = right
	return ans.next
if __name__=='__main__':
	A=ListNode(3)
	A.next = ListNode(1)
	A.next.next = ListNode(4)
	A.next.next.next = ListNode(48)
	A.next.next.next.next = ListNode(19)
	A.next.next.next.next.next = ListNode(28)

	B = sortlist(A)
	while B:
		print B.val
		B = B.next
