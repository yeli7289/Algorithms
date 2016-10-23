# heap sort O(nlogn), each heapify take O(n), and 
from heapq import heapify, heappop, heappush, heapreplace 
def heapify(A, n ,i):
	# construct the max heap
	largest = i
	left = 2*i+1
	right = 2*i+2
	# check if the left node is larger than the parent node
	if left<n and A[i]<A[left]:
		largest = left
	# check if the right node is larger than the largest node of left and parent
	if right<n and A[largest] < A[right]:
		largest = right
	# swap the root
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		heapify(A, n, largest) 
def heapSort(A):
	n = len(A)
	for i in range(n-1,-1,-1):
		if 2*i+1 < n:
			heapify(A, n, i)
	for i in range(n-1, 0, -1):
		A[i], A[0] = A[0], A[i]
		heapify(A, i, 0)
list=[1,5,6,4,10]
heapSort(list)
print list