class Solution(object):
    def coinChange(self, coins, amount):

        ans=-1
        dp=[[float('inf')]*(amount+1) for _ in range(len(coins))]
            
        for t in range(amount+1):
            if t % coins[0]==0:
                dp[0][t]=t//coins[0]


        for i in range(1,len(coins)):
            for j in range(amount+1):

                not_take=0+dp[i-1][j]
                take=float('inf')
                if coins[i] <= j:
                    take=1+dp[i][j-coins[i]]

                dp[i][j]=min(take,not_take)

        return ans if dp[len(coins)-1][amount] == float('inf') else dp[len(coins)-1][amount]


    
        