class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
       	adj=[[] for _ in range(numCourses)]
        visited=[False]*numCourses
        pathVisited=[False]*numCourses

        for u,v in prerequisites:
            
                adj[v].append(u)
                
        def dfs(node,parent):
            visited[node]=True
            pathVisited[node]=True
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour,node):
                        return True
                            
                elif pathVisited[neighbour]:
                    return True

            pathVisited[node]=False
                        
            return False
            
            
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i,-1):
                    return False
                    
        return True

            


