class Solution(object):
    def getBiggestThree(self, grid):
        m=len(grid)
        n=len(grid[0])
        output=set()
        for i in range(m):
            for j in range(n):
                output.add(grid[i][j])
                k=1
                while True:
                    if i-k <0 or i+k>=m or j-k < 0 or j +k >=n:
                        break
                    total=0
                    for distance in range(k):
                        total+=grid[i-k+distance][j+distance]
                        total+=grid[i+distance][j+k-distance]
                        total+=grid[i+k-distance][j-distance]
                        total+=grid[i-distance][j-k+distance]
                    k+=1
                    output.add(total)
        return sorted(output,reverse=True)[:3]

                
        


        
       
        