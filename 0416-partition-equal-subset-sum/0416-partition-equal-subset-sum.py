class Solution(object):
    def canPartition(self, nums):

        Total_sum=0
        for i in range(len(nums)):
            Total_sum+=nums[i]

        if Total_sum %2==1:
            return False


        dp=[[-1]*((Total_sum)//2+1) for _ in range(len(nums))]
        def solve(index,target):
            
            if target==0:
                return True
                
            if index==0:
                return nums[0]==target
                
            if dp[index][target] != -1:
                return dp[index][target]
                
            not_take=solve(index-1,target)
            
            take=False
            
            if target >= nums[index]:
                take=solve(index-1,target-nums[index])
                
            dp[index][target]=not_take or take
            
            return dp[index][target]

        return solve(len(nums)-1,Total_sum//2)
        
        
            


       
        