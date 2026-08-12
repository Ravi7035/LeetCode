class Solution(object):
    def maxSubarrayLength(self, nums, k):
        
        n=len(nums)
        maximum=0
        left=0
        freq={}

        for right in range(len(nums)):

            freq[nums[right]] =freq.get(nums[right],0)+1

            while freq[nums[right]] > k:
                freq[nums[left]]-=1
                left+=1

            maximum=max(right-left+1,maximum)

        return maximum

            
       