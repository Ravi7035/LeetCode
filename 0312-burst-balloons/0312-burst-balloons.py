class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)
        nums.insert(0,1)
        dp=[[-1]*len(nums) for _ in range(len(nums))]

        INT_MAX=-2**31


        def solve(i,j):
            if i > j:
                return 0    

            if dp[i][j] !=-1:
                return dp[i][j]

            maximum=INT_MAX

            for index in range(i,j+1):

                cost=nums[i-1]*nums[index]*nums[j+1] +solve(i,index-1) +solve(index+1,j)

                maximum=max(maximum,cost)

            dp[i][j]=maximum

            return dp[i][j]


        return solve(1,len(nums)-2)

        