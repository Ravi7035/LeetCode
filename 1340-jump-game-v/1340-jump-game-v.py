class Solution:
    def maxJumps(self, arr, d):

        n = len(arr)
        dp=[-1]*n

        def solve(i):

            maximum = 1

            if dp[i] !=-1:
                return dp[i]

            for j in range(i + 1, min(n, i + d + 1)):

                if arr[j] >= arr[i]:
                    break

                maximum = max(maximum, 1 + solve(j))

            for j in range(i - 1, max(-1, i - d - 1), -1):

                if arr[j] >= arr[i]:
                    break

                maximum = max(maximum, 1 + solve(j))

            dp[i]=maximum

            return dp[i]

        ans = 0

        for i in range(n):
            ans = max(ans, solve(i))

        return ans