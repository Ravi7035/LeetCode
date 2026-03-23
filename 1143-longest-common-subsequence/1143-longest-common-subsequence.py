class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m=len(text1)
        n=len(text2)
        dp=[[-1]*(n+1) for i in range(m)]

        def solve(index1,index2):

            if index1 ==m or index2==n:
                return 0

            if dp[index1][index2]!=-1:
                return dp[index1][index2]


            if text1[index1]==text2[index2]:

                dp[index1][index2]=1+solve(index1+1,index2+1)
            else:
    
                dp[index1][index2]=max(solve(index1+1,index2),solve(index1,index2+1))

            return dp[index1][index2]
        


        return solve(0,0)


        