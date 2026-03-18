class Solution(object):
    def minimumTotal(self, triangle):
        """
        n=len(triangle)
        memo={}
        
        def solve(i,j):
            if i==n-1:
                return triangle[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)]=triangle[i][j]+min(solve(i+1,j),solve(i+1,j+1))

            return memo[(i,j)]

        return solve(0,0)
        """

        
        #tabular approach 
        dp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=triangle[i][j]+min(dp[j],dp[j+1])

        return dp[0]
        




            
        
        
        

        