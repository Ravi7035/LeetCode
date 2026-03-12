# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        paths=[]
        def dfs(node,currentpath):
            if not node:
                return 

            char=chr(node.val+ord('a'))
            currentpath=char+currentpath

            if not node.left and not node.right:
                paths.append(currentpath)

            dfs(node.left,currentpath)
            dfs(node.right,currentpath)

        dfs(root,"")
        return min(paths)



            
         

       
        