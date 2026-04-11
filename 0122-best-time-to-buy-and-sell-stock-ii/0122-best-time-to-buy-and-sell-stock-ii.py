class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]

        #base cases

        dp[n][0]=dp[n][1]=0


        for index in range(n-1,-1,-1):
            for canBuy in range(2):

                if canBuy:
                    
                    
                        profit=max(-prices[index]+dp[index+1][0],0+dp[index+1][1])

                else:
                  
                        profit=max(prices[index]+dp[index+1][1],0+dp[index+1][0])


                dp[index][canBuy]=profit

        return dp[0][1]


        
        

       