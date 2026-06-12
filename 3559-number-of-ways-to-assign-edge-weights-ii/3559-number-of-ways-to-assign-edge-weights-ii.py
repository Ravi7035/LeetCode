class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = (n).bit_length()

        parent = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        def dfs(node, par):
            parent[node][0] = par

            for nei in graph[node]:
                if nei == par:
                    continue

                depth[nei] = depth[node] + 1
                dfs(nei, node)

        dfs(1, 0)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[i][j] = parent[parent[i][j - 1]][j - 1]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            return parent[u][0]

        ans = []

        for u, v in queries:

            ancestor = lca(u, v)

            dist = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow(2, dist - 1, MOD))

        return ans