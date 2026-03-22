class Solution(object):
    def findRotation(self, mat, target):
        n=len(mat)
        def isTrue(matrix):
            for row in matrix:
                row.reverse()
            if matrix==target:
                return True
            else:
                return False
            
        for x in range(4):
            for y in range(n):
                for z in range(y+1,n):
                    mat[y][z],mat[z][y]=mat[z][y],mat[y][z]

            if isTrue(mat):
                return True

        return False

        


        
        