# Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

# Analysis
This dfs solution is O(n^4), where n==9, we fill the value once a time, and go to the next level to see if we can solve the Sudoku, if can, return True and stop changing the board, if can't, change the value and try again. If we cannot find any value from 1 to 9 to fill, then return False.
# Code
```
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
    def dfs(self, board):
        def isVali(i, j , num):
            for col in range(9):
                if board[i][col]==num:
                    return False
            for row in range(9):
                if board[row][j]==num:
                    return False
            for row in range(3*(i/3), 3*(i/3+1)):
                for col in range(3*(j/3), 3*(j/3+1)):
                    if board[row][col]==num:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    continue
                for num in range(1,10):
                    # num can fill in [i][j] right now
                    if isVali(i, j, str(num)):
                        board[i][j] = str(num)
                        # fill the board and go a level deeper to see if we can solve the sudoku with this board[i][j]=num
                        if self.dfs(board):
                            return True
                        # if can't, reset board[i][j] to '.' and try another value
                        else:
                            board[i][j] = '.'
                # after trying all the possible value from 1 to 9, we still can't fill this block, then return False
                return False
        # no False happen when we finished filling all the block, then return True
        return True
```       