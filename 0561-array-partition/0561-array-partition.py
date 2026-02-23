class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        maximum_sum=0
        i=0

        while i < len(nums)-1:

            maximum_sum+=min(nums[i],nums[i+1])
            i+=2

        return maximum_sum
        