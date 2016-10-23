# N-Queens 2

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
# Analysis
similar to [N-Queens](https://github.com/yeli7289/Algorithms/wiki/N-Queens),

Added three bool lists for checking the valid position in O(1).
# Code
```
class Solution(object):
    count = 0
    column = []
    diag = []
    revdiag = []
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.column = [False for i in range(n)]
        self.diag = [False for i in range(2*n-1)]
        self.revdiag = [False for i in range(2*n-1)]
        C = [-1 for i in range(n)]
        
        self.dfs(C, 0, n)
        return self.count
    def dfs(self, C, row, n):
        def isVali(row, col, n):
            return not self.column[col] and not self.diag[row-col+n-1] and not self.revdiag[row+col]
            # for r in range(row):
            #     if C[r]==col:
            #         return False
            #     if abs(row-r)==abs(col-C[r]):
            #         return False
            # return True
        
        if row == n:
            self.count+=1
            return
        for col in range(n):
            if isVali(row, col, n):
                C[row] = col
                self.column[col], self.diag[row-col+n-1], self.revdiag[row+col] = True, True, True
                self.dfs(C, row+1, n)
                C[row] = -1
                self.column[col], self.diag[row-col+n-1], self.revdiag[row+col] = False, False, False