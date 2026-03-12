# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prefixSum={0:1}
        def dfs(node,CurrentSum):
            if not node:
                return 0
            CurrentSum+=node.val
            count=prefixSum.get(CurrentSum-targetSum,0)
            prefixSum[CurrentSum]=prefixSum.get(CurrentSum,0)+1

            count+=dfs(node.left,CurrentSum)
            count+=dfs(node.right,CurrentSum)

            prefixSum[CurrentSum]-=1

            return count

        return dfs(root,0)
        


       