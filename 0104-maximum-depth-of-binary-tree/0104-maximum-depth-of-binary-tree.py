# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # def dfs(node):
        #     if node is None:
        #       return 0

        #     left=dfs(node.left)
        #     right=dfs(node.right)

        #     return 1+max(left,right)


        # return dfs(root)
        
        from collections import deque
        if not root:
            return []
        
        q = deque([root])
        result = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)

        return len(result)



            

       
        