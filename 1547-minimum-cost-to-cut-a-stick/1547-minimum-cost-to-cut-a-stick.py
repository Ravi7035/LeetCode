class Solution(object):

    def minCost(self, n, cuts):

        cuts.insert(0, 0)
        cuts.append(n)

        cuts.sort()

        m = len(cuts)

        dp = [[-1] * m for _ in range(m)]

        INT_MAX = 2**31 - 1

        def solve(i, j):

            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            minimum = INT_MAX

            for index in range(i, j + 1):

                cost = (
                    cuts[j + 1] - cuts[i - 1]
                    + solve(i, index - 1)
                    + solve(index + 1, j)
                )

                minimum = min(minimum, cost)

            dp[i][j] = minimum

            return dp[i][j]

        return solve(1, m - 2)