# Selection Sort
# the left array is the sorted, and the right array is the unsorted,
# in each iteration, find the smallest one in the right and swap it with the leftmost element
def SelectionSort(A):
	for i in range(len(A)):
		samllest = A[i]
		index = i
		for j in range(i+1,len(A)):
			if A[j]<samllest:
				index = j
				samllest = A[j]
		swap(A,i,index)
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

list = [6,5,3,7,8,4,1,2,3,5]
SelectionSort(list)
print list