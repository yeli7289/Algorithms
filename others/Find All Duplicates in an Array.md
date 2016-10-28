# Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
Example
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```
# Analysis 
using O(n) memory is quite simple to solve this problem, we only need a dictionary.
However, we are asked to not to use extra space. The evidence that this array is range from 1 to n with size n, which means we can treat this array as our dictionary.

Ex. number 1 is recorded at position 0, number n is recorded at position n-1. The method to record is to add a "minus sign", which make sense and also don't change the original value.
Therefore, we negate the element to represent the first visit. nums[abs(nums[i])-1] = -nums[abs(nums[i])-1].
If we visit that index second time, we will find out it is a negative number, so that we know "nums[i]" is a duplicate.

# Code
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret= []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
               ret+=[abs(nums[i])] 
        return ret


