from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7

        n = len(edges) + 1

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            depth = 0

            for nei in adj[node]:
                if nei != parent:
                    depth = max(depth, 1 + dfs(nei, node))

            return depth

        d = dfs(1, -1)  # maximum depth in edges

        if d == 0:
            return 0

        return pow(2, d - 1, MOD)