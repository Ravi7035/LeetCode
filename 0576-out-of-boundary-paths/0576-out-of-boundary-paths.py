class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        Modulo=10**9+7
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]

        memo={}

        def solve(x,y,k):

            if x <0 or y <0 or x >=m or y >=n:
                return 1

            if k==0:
                return 0

            if (x,y,k) in memo:
                return memo[(x,y,k)]

            value=0

            for i in range(4):
                value=(value+solve(x+dx[i],y+dy[i],k-1))%Modulo

            memo[(x,y,k)]=value

            return memo[(x,y,k)]

        return solve(startRow,startColumn,maxMove)

        

            

            



            
                
                

            

            

        

      
        