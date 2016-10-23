class Solution:
	def quicksort(self, nums):
		self.helper(nums, 0, len(nums)-1)
	def helper(self, nums, left, right):
		index = self.partition(nums, left, right)
		if left < index-1:
			self.helper(nums, left, index-1)
		if index < right:
			self.helper(nums, index, right)

	def partition(self, nums, left, right):
		pivot = nums[(left+right)/2]

		while left<=right:
			while nums[left]<pivot:
				left+=1
			while nums[right]>pivot:
				right-=1
			if left<=right:
				swap(nums, left, right)
				left+=1
				right-=1
		return left	
def swap(nums, a, b):
	temp = nums[a]
	nums[a] = nums[b]
	nums[b] = temp
s=Solution()
nums=[4,3,4,5,5,6,2,1,2]
s.quicksort(nums)
print nums