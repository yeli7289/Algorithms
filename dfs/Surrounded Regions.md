# Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X

X O O X

X X O X

X O X X

After running your function, the board should be:

X X X X

X X X X

X X X X

X O X X

# Analysis
Searching start from the "O" on the boulder to every "O" that it can connect to. 
# Code
```
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(board, [(i,0)])
            if board[i][-1] == "O":
                self.dfs(board, [(i, len(board[0])-1)])
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.dfs(board, [(0, j)])
            if board[-1][j] == "O":
                self.dfs(board, [(len(board) - 1, j)])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'I':
                    board[i][j] = 'O'
                    
    def dfs(self, board, stack):
        round = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            i,j = stack.pop()
            board[i][j] = 'I'
            for (x, y) in round:
                nI, nJ = i + x, j + y
                if 0 <= nI < len(board) and 0 <= nJ < len(board[0]) and board[nI][nJ] == 'O':
                    stack += [(nI, nJ)]
```