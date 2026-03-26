class Solution(object):
    def canPartitionGrid(self, grid):
        from collections import Counter

        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        #build the frequency map of values using counter
        total_count = Counter(x for row in grid for x in row)

        top_sum = 0
        top_count = Counter()

        #horizontal cutting
        for i in range(m - 1):
            for val in grid[i]:
                top_sum += val
                top_count[val] += 1
                total_count[val] -= 1

            bottom_sum = total - top_sum
            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # remove from top
            if top_sum > bottom_sum and top_count[diff] > 0:
                rows, cols = i + 1, n
                if rows > 1 and cols > 1:
                    return True
                if rows == 1 and (grid[0][0] == diff or grid[0][n-1] == diff):
                    return True
                if cols == 1 and (grid[0][0] == diff or grid[i][0] == diff):
                    return True

            # remove from bottom
            if bottom_sum > top_sum and total_count[diff] > 0:
                rows, cols = m - i - 1, n
                if rows > 1 and cols > 1:
                    return True
                if rows == 1 and (grid[i+1][0] == diff or grid[i+1][n-1] == diff):
                    return True
                if cols == 1 and (grid[i+1][0] == diff or grid[m-1][0] == diff):
                    return True

        #vertical cutting
        total_count = Counter(x for row in grid for x in row)
        left_sum = 0
        left_count = Counter()

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_sum += val
                left_count[val] += 1
                total_count[val] -= 1

            right_sum = total - left_sum
            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            # remove from left
            if left_sum > right_sum and left_count[diff] > 0:
                rows, cols = m, j + 1
                if rows > 1 and cols > 1:
                    return True
                if rows == 1 and (grid[0][0] == diff or grid[0][j] == diff):
                    return True
                if cols == 1 and (grid[0][0] == diff or grid[m-1][0] == diff):
                    return True

            # remove from right
            if right_sum > left_sum and total_count[diff] > 0:
                rows, cols = m, n - j - 1
                if rows > 1 and cols > 1:
                    return True
                if rows == 1 and (grid[0][j+1] == diff or grid[0][n-1] == diff):
                    return True
                if cols == 1 and (grid[0][j+1] == diff or grid[m-1][j+1] == diff):
                    return True

        return False