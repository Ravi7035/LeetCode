# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        output=[-2**31]
        def dfs(node):
            if not node:
                return 0
            left=max(dfs(node.left),0)
            right=max(dfs(node.right),0)

            current=node.val+left+right
            output[0]=max(output[0],current)

            return node.val+max(left,right)

        dfs(root)

        return output[0]
            

        
      