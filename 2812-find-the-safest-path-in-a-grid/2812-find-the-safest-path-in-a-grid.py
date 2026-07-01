
class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 1: Multi-source BFS to compute distance to nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # If start or end is a thief, answer is 0
        if dist[0][0] == 0 or dist[n-1][n-1] == 0:
            return 0

        # Step 2: BFS to check if a path exists with safeness >= limit
        def canReach(limit):
            if dist[0][0] < limit:
                return False

            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q:
                r, c = q.popleft()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < n and
                        0 <= nc < n and
                        not visited[nr][nc] and
                        dist[nr][nc] >= limit):

                        visited[nr][nc] = True
                        q.append((nr, nc))

            return False

        # Step 3: Binary Search on the answer
        low = 0
        high = max(max(row) for row in dist)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans