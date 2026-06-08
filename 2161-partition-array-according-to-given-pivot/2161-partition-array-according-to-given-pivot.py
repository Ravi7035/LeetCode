class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        smaller_pivots=[]
        larger_pivots=[]

        for num in nums:
            if num < pivot:
                smaller_pivots.append(num)

            elif num > pivot:
                larger_pivots.append(num)

        Total_count=len(smaller_pivots)+len(larger_pivots)
        
        ans=[pivot]*(len(nums)-(Total_count))

        return smaller_pivots+ans+larger_pivots
        

        
        