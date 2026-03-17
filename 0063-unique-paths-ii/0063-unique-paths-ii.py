class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
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
       
        