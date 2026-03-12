# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node,CurrentSum):
            if node is None:
                return False

            CurrentSum+=node.val

            if not node.left and not node.right:
                return CurrentSum==targetSum

            return dfs(node.left,CurrentSum) or dfs(node.right,CurrentSum)

        return dfs(root,0)

        
            

       
        