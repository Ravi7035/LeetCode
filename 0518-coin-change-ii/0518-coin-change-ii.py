class Solution(object):
    def change(self, amount, coins):
        #memoization method 
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]

        #initializing the dp state 
        for i in range(n):
            dp[i][0]=1

        for t in range(amount+1):
            if t % coins[0] == 0:
                dp[0][t] = 1
            
        for index in range(1,n):
            for target in range(amount+1):

                not_take=dp[index-1][target]

                take=0

                if coins[index] <= target:

                    take=dp[index][target-coins[index]]

                dp[index][target]=not_take+take


        return dp[n-1][amount]