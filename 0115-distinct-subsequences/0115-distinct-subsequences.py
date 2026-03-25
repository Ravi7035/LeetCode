class Solution(object):
    def numDistinct(self, s, t):
        memo={}
        m=len(s)
        n=len(t)
        # def solve(i,j):
        #     if j <0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if s[i]==t[j]:
        #         memo[(i,j)]=solve(i-1,j-1)+solve(i-1,j)
        #         return memo[(i,j)]
        #     else:
        #         memo[(i,j)]=solve(i-1,j)
        #         return memo[(i,j)]

        # return solve(m-1,n-1)

        #tabulation method
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0]=1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

                else:
                    dp[i][j]=dp[i-1][j]

        return dp[m][n]



        
        



        


                
       