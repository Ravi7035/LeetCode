class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)

        next=[0,0]


        for index in range(n-1,-1,-1):
            curr=[0,0]       
            curr[1]=max(-prices[index]+next[0],0+next[1])
            curr[0]=max(prices[index]+next[1],0+next[0])

            next=curr

        return next[1]


        
        

       