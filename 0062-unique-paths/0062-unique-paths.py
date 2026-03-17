class Solution(object):
    def uniquePaths(self, m, n):
        memo={}
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)]=dfs(r, c+1) + dfs(r+1, c)
            return memo[(r,c)]

        return dfs(0, 0)