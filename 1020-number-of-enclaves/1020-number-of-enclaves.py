class Solution(object):
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        ans = 0

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] != 1 or
                (r, c) in visited
            ):
                return 0, False

            visited.add((r, c))

            size = 1

            touches_border = (
                r == 0 or r == rows - 1 or
                c == 0 or c == cols - 1
            )

            child_size, border = dfs(r + 1, c)
            size += child_size
            touches_border |= border

            child_size, border = dfs(r - 1, c)
            size += child_size
            touches_border |= border

            child_size, border = dfs(r, c + 1)
            size += child_size
            touches_border |= border

            child_size, border = dfs(r, c - 1)
            size += child_size
            touches_border |= border

            return size, touches_border

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size, touches_border = dfs(r, c)

                    if not touches_border:
                        ans += size

        return ans