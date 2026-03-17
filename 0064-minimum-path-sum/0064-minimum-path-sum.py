class Solution(object):
    def minPathSum(self, grid):
        #using memoization 
        m=len(grid)
        n=len(grid[0])
        """
        minimum_sum=0
        memo={}
        def dfs(r,c):
            if r <0 or c <0:
                return float('inf')
            if r==0 and c==0:
                return grid[0][0]

            if (r,c) in memo:
                return memo[(r,c)]
            

            memo[(r,c)]=grid[r][c]+min(dfs(r-1,c),dfs(r,c-1))

            return memo[(r,c)]

        return dfs(m-1,n-1)
        """

        #using tabulation method
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for r in range(m):
            for c in range(n):
                if r ==0 and c==0:
                    continue
                elif r==0:
                    dp[r][c]=grid[r][c]+dp[r][c-1]
                elif c==0:
                    dp[r][c]=grid[r][c]+dp[r-1][c]
                else:
                    dp[r][c]=grid[r][c]+min(dp[r-1][c],dp[r][c-1])
        return dp[m-1][n-1]
                
            
            

            

            
        
       
        