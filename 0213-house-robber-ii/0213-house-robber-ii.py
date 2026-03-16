class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(arr):
            m=len(arr)
            dp=[-1]*m
            def robb(i):
                if i==0:
                    return arr[0]
                if i<0:
                    return 0
                if dp[i]!=-1:
                    return dp[i]
                pick=arr[i]+robb(i-2)
                leave=robb(i-1)
                dp[i]=max(pick,leave)
                return dp[i]
            return robb(m-1)

        case1=solve(nums[:-1])
        case2=solve(nums[1:])
        return max(case1,case2)
