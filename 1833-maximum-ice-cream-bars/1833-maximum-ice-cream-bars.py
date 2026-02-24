class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        costs.sort()
        count=0
        for i in range(len(costs)):
            if coins >=costs[i]:
                count+=1
                coins-=costs[i]
        return count
        """

        #through the counting sort 

        ans=0

        count_array=[0]*(max(costs)+1)

        for i in range(len(costs)):
            
            count_array[costs[i]]+=1

        result=[]

        for i in range(len(count_array)):

            result.extend([i]*count_array[i])

        for i in range(len(result)):

            if coins >=result[i]:
                ans+=1
                coins-=result[i]

            else:
                break

    
        return ans 


            
        
       