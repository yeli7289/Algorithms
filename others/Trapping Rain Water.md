# Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Analysis
Using two pointers to keep track of how much water can it holds. Search from left of right to maintain a max height, and sum up the water with width in 1. 
# Code
```
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        maxleft, maxright = 0, 0
        ret = 0
        while left<right:
            if height[left]<=height[right]:
                if height[left]>=maxleft: maxleft=height[left]
                else: ret+=maxleft-height[left]
                left+=1
            else:
                if height[right]>=maxright: maxright=height[right]
                else: ret+=maxright-height[right]
                right-=1
        return ret
        
```