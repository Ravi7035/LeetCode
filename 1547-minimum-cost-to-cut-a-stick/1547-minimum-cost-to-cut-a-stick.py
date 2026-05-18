class Solution(object):

    def minCost(self, n, cuts):

        cuts.insert(0, 0)
        cuts.append(n)

        cuts.sort()

        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        INT_MAX = 2**31 - 1

        for i in range(m-2,0,-1):
            for j in range(1,m-1):

                if i > j:
                    continue

                minimum = INT_MAX

                for index in range(i, j + 1):

                    cost = (
                        cuts[j + 1] - cuts[i - 1]
                        + dp[i][index - 1]
                        + dp[index + 1][j]
                    )

                    minimum = min(minimum, cost)


                dp[i][j]=minimum


        return dp[1][m-2]