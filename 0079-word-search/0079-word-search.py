class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])

        visited=[[False]*n for _ in range(m)]

        def solve(i,j,index):

            if index==len(word):
                return True

                
            if i < 0 or i >= m or j < 0 or j >= n:
                return False


            if visited[i][j]:
                return False

          
            if board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            visited[i][j]=True

            directions=[(0,1),(0,-1),(1,0),(-1,0)]

            for dx,dy in directions:

                nx=i+dx
                ny=j+dy

                if 0<=nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if solve(nx,ny,index+1):
                            return True


            visited[i][j]=False

            return False


        for i in range(m):
            for j in range(n):
                if solve(i,j,0):
                    return True

        return False








        