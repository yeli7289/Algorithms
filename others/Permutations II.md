# Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```
# Code
```
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        self.dfs(sorted(nums), [], ret, len(nums))
        return ret
    def dfs(self, nums, path, ret, l):
        if len(path) == l:
            ret.append(path)
            return
        for i, num in enumerate(nums):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[num], ret, l)
            
```