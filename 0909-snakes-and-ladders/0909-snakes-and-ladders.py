class Solution(object):
    def snakesAndLadders(self, board):
        n=len(board)
        target= n*n
        visited=[False]* (target +1)
        q=deque([(1,0)])
        visited[1]=True

        #row,col conversion

        def convert(num):
            row = n - 1 - (num - 1) // n
            col = (num - 1) % n

            if (n-1-row) % 2 == 1:
                col = n - 1 - col

            return row,col

        while q:
            cell,throws=q.popleft()

            if cell==target:
                return throws
            
            for i in range(1,7):

                next_step=cell+i

                if next_step > n*n:
                    continue

                row,col=convert(next_step)

                if board[row][col] != -1:
                    next_step=board[row][col]

                if not visited[next_step]:
                    visited[next_step]=True
                    q.append((next_step,throws+1))

        return -1

            

            


      