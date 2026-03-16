class Solution(object):
    def climbStairs(self, n):
        dp=[-1]*n
        def solve(i):
            if i ==n:
                return 1
            if i > n:
                return 0
            if dp[i] !=-1:
                return dp[i]
            dp[i]=solve(i+1)+solve(i+2)
            return dp[i]

        return solve(0)
       