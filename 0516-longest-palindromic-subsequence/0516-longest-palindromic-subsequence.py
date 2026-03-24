class Solution(object):
    def longestPalindromeSubseq(self, s):
        m=len(s)
        dp=[[-1]*m for _ in range(m)]

        #initializing the dp state

        for i in range(m):
            dp[i][i]=1
        

        for length in range(2,m+1):
            for i in range(m-length+1):
                j=i+length-1

                if s[i]==s[j]:
                    
                    dp[i][j]=2+dp[i+1][j-1] if length > 2 else 2 

                else:


                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])


        return dp[0][m-1]
        

           

            

            


                

            
        
        