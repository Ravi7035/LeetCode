class Solution(object):
    def minDistance(self, word1, word2):

        m=len(word1)
        n=len(word2)
        dp=[[-1]*(n+1) for i in range(m+1)]

        def solve(index1,index2):

            if index1 ==m or index2==n:
                return 0

            if dp[index1][index2]!=-1:
                return dp[index1][index2]


            if word1[index1]==word2[index2]:

                dp[index1][index2]=1+solve(index1+1,index2+1)
            
            else:
    
                dp[index1][index2]=max(solve(index1+1,index2),solve(index1,index2+1))

            return dp[index1][index2]

        res=solve(0,0)

        return m-res+(n-res)
        



        
        