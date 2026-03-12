# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        paths=[]
        def dfs(node,currentpath):
            if not node:
                return 
            currentpath=currentpath + str(node.val)
            if not node.left and not node.right:
                paths.append(currentpath)
                return 
            currentpath+="->"
            dfs(node.left,currentpath)
            dfs(node.right,currentpath)
        dfs(root,"")
        return paths

      
        