class Solution(object):

    def lengthOfLIS(self, nums):

        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # fill from back
        for index in range(n - 1, -1, -1):

            for prev_index in range(index - 1, -2, -1):

                # skip current
                not_take = dp[index + 1][prev_index + 1]

                take = 0

                # take current
                if prev_index == -1 or nums[index] > nums[prev_index]:

                    take = 1 + dp[index + 1][index + 1]

                dp[index][prev_index + 1] = max(take, not_take)

        return dp[0][0]