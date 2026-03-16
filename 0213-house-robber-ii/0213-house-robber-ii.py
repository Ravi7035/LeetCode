class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(arr):
           
            m=len(arr)
            if m==1:
                return arr[0]
        
            dp=[-1]*m
            def robb():
                dp[0]=arr[0]
                dp[1]=max(arr[0],arr[1])
                for i in range(2,m):
                    dp[i]=max(dp[i-2]+arr[i],dp[i-1])
                return dp[m-1]
            return robb()
            
        case1=solve(nums[:-1])
        case2=solve(nums[1:])
        return max(case1,case2)
