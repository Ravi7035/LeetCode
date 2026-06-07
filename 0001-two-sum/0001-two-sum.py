class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        register={}

        for i,num in enumerate(nums):
            complement=target-num

            if complement in register:
                return [i,register[complement]]


            register[num]=i

      
        
        