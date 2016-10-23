# bubble up the smallst element one by one iteration
# O(n^2) O(1) extra space
def bubblesort(A):
	for i in range(len(A)):
		for j in range(len(A)-1,i,-1):
			if A[j] < A[j-1]:
				swap(A, j, j-1)
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

list = [4,3,2,2,1,4]
bubblesort(list)
print list