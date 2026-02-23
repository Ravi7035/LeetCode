class Solution(object):
    def candy(self, ratings):

        candies=[1]*len(ratings)

        #satisfying the conditions from left to right

        for i in range(1,len(ratings)):

            if ratings[i] > ratings[i-1]:

                candies[i]=candies[i-1]+1

        #satisfying the conditions from right to left

        for i in range(len(ratings)-2,-1,-1):

            if ratings[i]> ratings[i+1]:

                candies[i]=max(candies[i],candies[i+1]+1)

        return sum(candies)





       