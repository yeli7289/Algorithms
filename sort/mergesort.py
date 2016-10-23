class Solution:
	def mergesort(self, nums):
		self.helper(nums, 0, len(nums)-1)
	def helper(self, nums, left, right):
		mid = (left+right)/2
		if left < right:
			self.helper(nums, left, mid)
			self.helper(nums, mid+1, right)
			self.merge(nums, left, mid, right)

	def merge(self, nums, left, mid, right):
		hl, hr = left, mid+1
		temp = [None]*(right-left+1)
		i = 0
		while hl<=mid and hr<=right:
			if nums[hl]<nums[hr]:
				temp[i] = nums[hl]
				hl+=1
			else:
				temp[i] = nums[hr]
				hr+=1
			i+=1
		if hl <= mid:
			temp[i:] = nums[hl:mid+1]
		if hr <= right:
			temp[i:] = nums[hr:right+1]
		i = 0
		while left <= right:
			nums[left] = temp[i]
			left+=1
			i+=1
s=Solution()
nums = [3,2,1,4,5]
s.mergesort(nums)
print nums