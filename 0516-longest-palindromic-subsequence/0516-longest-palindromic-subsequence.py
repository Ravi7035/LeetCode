class Solution(object):
    def longestPalindromeSubseq(self, s):
        m=len(s)
        dp=[[-1]*m for _ in range(m)]
        def solve(i,j):
            if i > j:
                return 0

            if i==j:
                return 1

            if dp[i][j] !=-1:
                return dp[i][j]
            
            if s[i]==s[j]:
                
                dp[i][j]=2+solve(i+1,j-1)
            else:
                dp[i][j]=max(solve(i+1,j),solve(i,j-1))

            return dp[i][j]

        return solve(0,m-1)
        

           

            

            


                

            
        
        