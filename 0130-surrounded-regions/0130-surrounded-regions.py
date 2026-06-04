class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=set()
        def dfs(r,c,component):
            
            if r < 0 or r >=m or c < 0 or c >=n or board[r][c] != "O" or (r,c) in visited:
                return False

            visited.add((r,c))
            component.append((r,c))

            boundary=(r==0 or c==0 or r==m-1 or c==n-1)

            boundary|=dfs(r,c+1,component)
            boundary|=dfs(r+1,c,component)
            boundary|=dfs(r,c-1,component)
            boundary|=dfs(r-1,c,component)

            return boundary


        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in visited:
                    component=[]
                    isboundary=dfs(i,j,component)

                    if not isboundary:
                        
                        for x,y in component:
                            board[x][y]="X"

        return board


        



            
            
            

        