class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[0]*(n+1)
        INT_MAX=2**31-1


        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):

            for j in range(i, n):

                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp[n]=0

        
        for i in range(n-1,-1,-1):

            minimum=INT_MAX


            for j in range(i,n):

                if pal[i][j]:

                    cost=1+dp[j+1]

                    minimum=min(minimum,cost)


            dp[i]=minimum

        return dp[0] - 1
