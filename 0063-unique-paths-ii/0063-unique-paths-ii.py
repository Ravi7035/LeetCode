class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        """
        memo={}
        def dfs(r,c):
            if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
                return 0
            if r==0 and c==0:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r,c)]=dfs(r-1,c)+dfs(r,c-1)
            return memo[(r,c)]
        return dfs(m-1,n-1)
        """

        #tabualtion method
        dp=[[0]*n for _ in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]==1:
                    dp[r][c]=0
                else:
                    if r >0:
                        dp[r][c]+=dp[r-1][c]
                    if c >0:
                        dp[r][c]+=dp[r][c-1]

        return dp[m-1][n-1]
            


       
        