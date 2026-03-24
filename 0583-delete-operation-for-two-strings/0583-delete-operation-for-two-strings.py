class Solution(object):
    def minDistance(self, word1, word2):

        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for i in range(m+1)]

        for index1 in range(1,m+1):
            for index2 in range(1,n+1):


                if word1[index1-1]==word2[index2-1]:

                    dp[index1][index2]=1+dp[index1-1][index2-1]
                
                else:
        
                    dp[index1][index2]=max(dp[index1-1][index2],dp[index1][index2-1])

        res=dp[m][n]

        return m-res+(n-res)
        



        
        