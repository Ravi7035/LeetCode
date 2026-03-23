class Solution(object):
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]

        def solve(i, j):
            # Out of bounds → ignore path
            if i >= m or j >= n:
                return None

            # Destination
            if i == m - 1 and j == n - 1:
                return [grid[i][j], grid[i][j]]

            if dp[i][j] is not None:
                return dp[i][j]

            val = grid[i][j]

            right = solve(i, j + 1)
            down = solve(i + 1, j)

            candidates = []

            # Collect valid paths only
            if right:
                candidates.append(val * right[0])
                candidates.append(val * right[1])

            if down:
                candidates.append(val * down[0])
                candidates.append(val * down[1])

            # Store max and min
            dp[i][j] = (max(candidates), min(candidates))
            return dp[i][j]

        res = solve(0, 0)

        # If no valid path
        if res is None:
            return -1

        max_product = res[0]

        return -1 if max_product < 0 else max_product % (10**9 + 7)