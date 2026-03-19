class Solution(object):
    def numberOfSubmatrices(self, grid):
        m=len(grid)
        n=len(grid[0])
        prefix=[[0]*n for _ in range(m)]
        countX=[[0]*n for _ in range(m)]
        res=0
        for row in range(m):
            for col in range(n):
                value=0

                if grid[row][col]=="X":
                    value=1
                if grid[row][col]=="Y":
                    value=-1

                x=1 if grid[row][col]=="X" else 0

                prefix[row][col]=value
                countX[row][col]=x

                if row >0:
                    prefix[row][col]+=prefix[row-1][col]
                    countX[row][col]+=countX[row-1][col]

                if col >0:
                    prefix[row][col]+=prefix[row][col-1]
                    countX[row][col]+=countX[row][col-1]

                if row>0 and col >0:
                    prefix[row][col]-=prefix[row-1][col-1]
                    countX[row][col]-=countX[row-1][col-1]
            
                if prefix[row][col]==0 and countX[row][col] >0:
                    res+=1

        return res
                

                

                    

                

                
                

        
        