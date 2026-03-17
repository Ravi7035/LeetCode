class Solution(object):
    def numIslands(self, grid):
        rows, columns = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)

        output = [0]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    output[0] += 1
                    dfs(r, c)

        return output[0]