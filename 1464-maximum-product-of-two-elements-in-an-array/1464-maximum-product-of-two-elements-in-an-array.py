class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max=float("-inf")
        second_max=float("-inf")

        for i in range(len(nums)):
            if nums[i] > first_max:
                second_max=first_max
                first_max=nums[i]

            elif nums[i] > second_max:
                second_max= nums[i]

        return (first_max -1) * ( second_max -1)
            

       