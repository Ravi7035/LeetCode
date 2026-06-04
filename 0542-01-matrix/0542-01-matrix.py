class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        
        q=deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=-1

        
        directions=[(0,-1),(1,0),(0,1),(-1,0)]

        while q:
            r,c=q.popleft()

            for x,y in directions:
                nr,nc=x+r,y+c

                if (nr >=0 and nr < m and nc >=0 and nc < n) and mat[nr][nc]==-1:
                    mat[nr][nc]=mat[r][c]+1
                    q.append((nr,nc))
        
        return mat


        
        