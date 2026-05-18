class Solution(object):

    def maximalSquare(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[-1] * cols for _ in range(rows)]

        maximum = [0]

        def solve(i, j):

            # out of bounds
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            up = solve(i - 1, j)
            left = solve(i, j - 1)
            diag = solve(i - 1, j - 1)

            if matrix[i][j] == '1':

                dp[i][j] = 1 + min(up, left, diag)

                maximum[0] = max(maximum[0], dp[i][j])

            else:
                dp[i][j] = 0

            return dp[i][j]

        for i in range(rows):
            for j in range(cols):
                solve(i, j)

        return maximum[0] * maximum[0]