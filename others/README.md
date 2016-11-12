# Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
# 
# Code
```
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)-1
        for i in range(len(matrix)/2):
            matrix[i], matrix[l-i] = matrix[l-i], matrix[i]
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
```

