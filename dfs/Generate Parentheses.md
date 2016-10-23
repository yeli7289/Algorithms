# Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Analysis
Think of this as a dfs problem, in each node you have 2 choices to go for, '(' or ')', 

The constraints are: 
* if the number of '(' you use is under n, then you can go for '(' .
* if the number of '(' is more than ')' you have used so far, you can go for ')'

# Code
```
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.dfs("(", ret, 1, 0, n)
        return ret
    def dfs(self, path, ret, n_left, n_right, n):
        if n_left==n:
            ret.append(path+")"*(n-n_right))
            return
        self.dfs(path+"(", ret, n_left+1, n_right, n)
        if n_left>n_right:
            self.dfs(path+")", ret, n_left, n_right+1, n)
```               