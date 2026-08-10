class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m=len(dungeon)
        n=len(dungeon[0])
        minimum=float("-inf")

        dp=[[-1]* (n+1) for _ in range(m+1)]
        def solve(i,j):

            if dp[i][j] != -1:
                return dp[i][j]

            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])

            if i >= m or j >= n:
                return float("inf")

            right = solve(i + 1, j)
            down = solve(i, j + 1)

            need = min(right, down)

            dp[i][j]= max(1, need - dungeon[i][j])

            return dp[i][j]


        return solve(0,0) 

        

            

            

            

        