class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)

        maximum=max(nums)
        minimum=min(nums)

        return (maximum-minimum)*k

        
        