class Solution(object):
    def minPathSum(self, grid):
        #using memoization 
        m=len(grid)
        n=len(grid[0])
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
            
            

            

            
        
       
        