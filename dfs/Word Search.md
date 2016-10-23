# Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

# Analysis
DFS traverse with early termination, a node in the tree return true when one of its child nodes is true (valid).
# Code 
```
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        # keep track of the word grid
        self.track = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, '', i, j, len(board)-1, len(board[0])-1):
                    return True
        return False

    def dfs(self, board, word, i, j, m_row, m_col):
        if i > m_row or i<0 or j > m_col or j<0:
            return False
        if self.track[i][j]:
            return False
        if board[i][j]!=self.word[len(word)]:
            return False
        w = board[i][j]
        if word+w==self.word:
            return True
        self.track[i][j] = True
        ret = self.dfs(board, word+w, i+1, j, m_row, m_col) or \
        self.dfs(board, word+w, i-1, j, m_row, m_col) or \
        self.dfs(board, word+w, i, j+1, m_row, m_col) or \
        self.dfs(board, word+w, i, j-1, m_row, m_col)
        self.track[i][j] = False
        return ret
        
```