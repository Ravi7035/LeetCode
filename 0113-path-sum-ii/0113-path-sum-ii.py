# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        output=[]
        def dfs(node,CurrentSum,CurrentPath):
            if not node:
                return
            CurrentSum+=node.val
            CurrentPath.append(node.val)
            if not node.left and not node.right:
                if CurrentSum==targetSum:
                    output.append(CurrentPath[:])

            dfs(node.left,CurrentSum,CurrentPath)
            dfs(node.right,CurrentSum,CurrentPath)
            CurrentPath.pop()
        dfs(root,0,[])
        return output
                    


       
        