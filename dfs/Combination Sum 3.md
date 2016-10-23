# Combination Sum 3
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Code
```
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret=[]
        self.dfs(1, [], ret, k, n);
        return ret
        
    def dfs(self, s, path, ret, k, n) :
        if n==0 and k==0:
            ret.append(path)
            return
        if k==0:
            return
        for i in range(s,10):
            # early termination
            if i>n or (k*i>n):
                break
            self.dfs(i+1, path+[i], ret, k-1, n-i)
```