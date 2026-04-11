class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)

        dp=[[[0]*(3) for _ in range(2)] for _ in range(n+1)]
        
        #base cases 

        for index in range(n-1,-1,-1):
            for canBuy in range(2):
                for transactions in range(1,3):

                    if canBuy:
                        profit=max(-prices[index]+dp[index+1][0][transactions],0+dp[index+1][1][transactions])

                    else:
                        profit=max(prices[index]+dp[index+1][1][transactions-1],0+dp[index+1][0][transactions])

                    dp[index][canBuy][transactions]=profit


        return dp[0][1][2]

            


       
        