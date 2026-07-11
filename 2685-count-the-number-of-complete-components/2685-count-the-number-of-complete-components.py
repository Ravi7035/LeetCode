class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #build the graph 

        graph=defaultdict(list)

        for u,v in edges:

            graph[u].append(v)
            graph[v].append(u)

        #dfs function to get the connected components

        visited=set()
        ans=0

        def dfs(node):
            visited.add(node)
            nodes.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        
        #calculating module to get the complete connected components

        for i in range(n):
            if i not in visited:
                nodes=[]
                dfs(i)

                k=len(nodes)

                actual=0

                for node in nodes:
                    actual += len(graph[node])

                actual//=2

                expected= (k*(k-1))//2

                if actual == expected:
                    ans+=1

        return ans
                


                
                


        
        