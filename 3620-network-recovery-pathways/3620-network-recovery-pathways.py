class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n=len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        maxCost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            maxCost = max(maxCost, c)

        # Topological order
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = float("inf")

        def check(x):
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                # offline intermediate node
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, c in graph[u]:
                    if c < x:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dp[u] + c < dp[v]:
                        dp[v] = dp[u] + c

            return dp[n - 1] <= k

        lo = 0
        hi = maxCost
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans