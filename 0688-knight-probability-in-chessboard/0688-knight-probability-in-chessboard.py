class Solution(object):
    def knightProbability(self, n, k, row, column):
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]

        memo={}

        def solve(x,y,k):

            if x <0 or y <0 or x >= n or y >=n:

                return 0

            if k==0:
                return 1

            
            if (x,y,k) in memo:
                return memo[(x,y,k)]

            probability=0
            for i in range(8):
                probability+=solve(x+dx[i],y+dy[i],k-1)/8.0

            memo[(x,y,k)]=probability
            return memo[(x,y,k)]

        return solve(row,column,k)         



        
        