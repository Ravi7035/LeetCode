class Solution(object):
    def canPartitionGrid(self, grid):
        m=len(grid)
        n=len(grid[0])
        #total sum
        total=0
        for i in range(m):
            for j in range(n):
                total+=grid[i][j]

        if total %2==1:
            return False

        target=total//2

        #prefix sum the matrix rows for horizontal cut
        prefix_sum=0
        for row in grid:
            prefix_sum+=sum(row)

            if prefix_sum==target:
                return True

        #filling up the sum of each column 

        column_sum=[0]*n

        for i in range(m):
            for j in range(n):
                column_sum[j]+=grid[i][j]

        prefix_sum=0

        for i in range(n):
            prefix_sum+=column_sum[i]

            if prefix_sum==target:
                return True

        return False
        




        
       
        