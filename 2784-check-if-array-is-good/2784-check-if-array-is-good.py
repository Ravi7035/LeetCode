class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_element=max(nums)
        no_of_ele=max_element+1
        if len(nums)!=no_of_ele:
            return False


        sorted_array=nums.sort()

        curr=1

        for i in range(len(nums)-1):
            if curr!=nums[i]:
                return False
            curr+=1
        
        if nums[-1]!=max_element:
            return False

        return True

        

        

        