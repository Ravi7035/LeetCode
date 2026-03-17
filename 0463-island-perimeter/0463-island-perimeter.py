class Solution(object):
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            
            grid[r][c] = -1 
            
            return (dfs(r-1, c) +
                    dfs(r+1, c) +
                    dfs(r, c-1) +
                    dfs(r, c+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
                    """


        #optimized math solution
        perimeter=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    perimeter+=4
                    if r+1 < rows and grid[r+1][c]==1:
                        perimeter-=2
                    if c+1 < cols and grid[r][c+1]==1:
                        perimeter-=2

        return perimeter