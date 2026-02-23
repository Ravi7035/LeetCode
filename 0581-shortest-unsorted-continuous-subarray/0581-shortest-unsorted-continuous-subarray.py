class Solution(object):
    def findUnsortedSubarray(self, nums):
        maximum_till_now=nums[0]
        minimum_till_now=nums[-1]
        start=-1
        end=-2

        for i in range(1,len(nums)):

            maximum_till_now=max(maximum_till_now,nums[i])

            if nums[i] < maximum_till_now:

                end=i

        for i in range(len(nums)-1,-1,-1):

            minimum_till_now=min(minimum_till_now,nums[i])
            
            if nums[i] > minimum_till_now:

                start=i

        return end-start+1

        
        