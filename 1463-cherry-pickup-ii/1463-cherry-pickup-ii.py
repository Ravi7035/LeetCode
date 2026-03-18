class Solution(object):
    def cherryPickup(self, grid):
        m=len(grid)
        n=len(grid[0])
        memo={}

        def solve(i,j1,j2):
            if j1 < 0 or j2 <0 or j1 >=n or j2 >=n:
                return float('-inf')
            if i==m-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]

            if (i,j1,j2) in memo:
                return memo[(i,j1,j2)]
            

            maximum=float('-inf')

            for varJ1 in range(-1,2):
                for varJ2 in range(-1,2):

                    value=grid[i][j1] if j1==j2 else grid[i][j1]+grid[i][j2]
                    value+=solve(i+1,j1+varJ1,j2+varJ2)
                    maximum=max(maximum,value)
                    memo[(i,j1,j2)]=maximum

            return memo[(i,j1,j2)]

        return solve(0,0,n-1)


                 
            
            
      