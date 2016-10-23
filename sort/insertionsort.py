# Insertion sort O(n^2), works well when the array is nearly sorted
# in place, no need for extra space
def InsertionSort(A):
	for i in range(1,len(A)):
		current = A[i]
		k = i
		# find the right place to insert
		while k>0 and A[k-1]>current:
			A[k] = A[k-1]
			k = k-1
		A[k] = current
list = [4,5,657,6,45,45,3,4,7]
InsertionSort(list)
print list