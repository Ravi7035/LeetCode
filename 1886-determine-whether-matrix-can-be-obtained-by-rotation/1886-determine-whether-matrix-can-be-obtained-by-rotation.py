class Solution(object):
    def findRotation(self, mat, target):
        """
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
        """

        #single pass method

        #comparing the exact element when the mat is rotated by 4 angles 0,90,180,270

        n=len(mat)

        rot0=rot90=rot180=rot270=True

        for i in range(n):
            for j in range(n):
                
                if mat[i][j] != target[i][j]:
                    rot0 = False
                
                if mat[i][j] != target[j][n-1-i]:
                    rot90 = False
                
                if mat[i][j] != target[n-1-i][n-1-j]:
                    rot180 = False
                
                if mat[i][j] != target[n-1-j][i]:
                    rot270 = False

        return rot0 or rot90 or rot180 or rot270
        





        


        
        