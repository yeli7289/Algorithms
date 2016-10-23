# N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# Analysis

In a single row, there is one queen, on more and on less, since we want to have N queens in a N*N chessboard. The same critria for column.
A diagonal is not allowed to have two queen.

This is a typical DFS question since we are asked to give "all possible solution", so the way to deal with this task is to loop trought each row and column to see if it is possible to place a queen here and go further.

I use row here to do recursive dfs search, if we find a possible spot for the queen in that row, we record it and go to the next row.

The terminal condition is set when row==n, and we then append the solution to the ret list.

# Code
`
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        C = [-1 for i in range(n)]
        ret = []
        self.dfs(C, 0, ret, n)
        return ret
    def dfs(self, C, row, ret, n):
        def isVali(row, col):
            for r in range(row):
                if C[r]==col:
                    return False
                if abs(row-r)==abs(col-C[r]):
                    return False
            return True
            
        if row==n:
            ans = []
            for i in range(n):
                ans.append('.'*C[i]+'Q'+'.'*(n-1-C[i]))
            ret.append(ans)
            return
        for col in range(n):
            if isVali(row, col):
                C[row] = col
                self.dfs(C, row+1, ret, n)
                C[row] = -1
`


