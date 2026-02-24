class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        Temp_sum=sum(cost)
        i=2

        while i < len(cost):

            Temp_sum-=cost[i]
            i+=3
        return Temp_sum


       

        


        

       