class Solution(object):
    def change(self, amount, coins):
        #memoization method 
        n=len(coins)
        dp=[0]*(amount+1)

        dp[0]=1

        for coin in coins:
            for target in range(coin,amount+1):
                dp[target]+=dp[target-coin]

        return dp[amount]