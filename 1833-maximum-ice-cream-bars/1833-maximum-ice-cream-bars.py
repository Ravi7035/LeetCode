class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        for i in range(len(costs)):
            if coins >=costs[i]:
                count+=1
                coins-=costs[i]

        return count
        
       