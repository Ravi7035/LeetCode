class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        #buiding the gtaph 

        graph=defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        q=deque([1])
        visited={1}

        minimum=float('inf')

        while q:
            node = q.popleft()

            for nei,w in graph[node]:
                minimum=min(minimum,w)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return minimum

        