# Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
# Analysis
Use BFS and keep track of how deep you go. 
# Code
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [beginWord]
        dist = 1
        level, nextlevel = 1, 0
        wordList.remove(beginWord)
        if len(beginWord)!=len(endWord):
            return 0
        while queue:
            word = queue.pop()
            level-=1
            for k in range(len(word)):
                for i in range(26):
                    c = chr(ord('a')+i)
                    w = word[:k]+c+word[k+1:]
                    if w == endWord:
                        return dist+1
                    if w in wordList:
                        queue.insert(0,w)
                        wordList.remove(w)
                        nextlevel+=1
            if level == 0:
                dist += 1
                level, nextlevel = nextlevel, 0
        return 0