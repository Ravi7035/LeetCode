class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        dp=[[-1]*2 for _ in range(n+1)]
        def solve(index,canBuy):
            if index>=n:
                return 0

            if dp[index][canBuy] !=-1:
                return dp[index][canBuy]
            
            if canBuy:

                profit=max(-prices[index]+solve(index+1,0),0+solve(index+1,1))

            else:
                profit=max((prices[index]-fee)+solve(index+1,1),0+solve(index+1,0))

            dp[index][canBuy]=profit

            return dp[index][canBuy]

        return solve(0,1)
       
        
        