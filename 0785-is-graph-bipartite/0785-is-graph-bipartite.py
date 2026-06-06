class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        color=[-1]*n

        for start in range(n):

            if color[start]!=-1:
                continue

            q=deque([start])
            color[start]=0

            while q:
                node=q.popleft()
                
                for nei in graph[node]:
                    if color[nei]==-1:
                        color[nei]=1-color[node]
                        q.append(nei)

                    elif color[nei] == color[node]:
                        return False

        return True

                    
        
        