class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
    
        for row in range(m):
            for col in range(row+1,n):
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]

        for row in range(m):
            left=0
            right=n-1
            while left < right:
                matrix[row][left],matrix[row][right]=matrix[row][right],matrix[row][left]
                left+=1
                right-=1

        return matrix
        