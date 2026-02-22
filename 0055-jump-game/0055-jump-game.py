class Solution(object):
    def canJump(self, nums):
        max_reachable=0

        for i in range(len(nums)):

            if i <= max_reachable:

                max_reachable=max(max_reachable,i+nums[i])

            else:

                return False


        return True
       

       



                
       