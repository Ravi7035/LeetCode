class Solution(object):
    def climbStairs(self, n):
        """
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
        """
        #optimized o(1) space solution(tabulation method)
        prev1=1
        prev2=2
        if n<=2:
            return n
        for i in range(3,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr

        return prev2
            

        
            
            
            

