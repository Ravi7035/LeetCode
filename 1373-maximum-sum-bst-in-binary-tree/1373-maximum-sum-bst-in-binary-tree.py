# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans=[0]
        def solve(root):
            if not root:
                return True,float('inf'),float('-inf'),0

            left_bst,left_min,left_max,left_Sum=solve(root.left)
            right_bst,right_min,right_max,right_Sum=solve(root.right)

            if left_bst and right_bst and left_max < root.val < right_min:

                curr_sum=left_Sum+right_Sum+root.val
                ans[0]=max(ans[0],curr_sum)

                return (
                    True,
                    min(left_min,root.val),
                    max(right_max,root.val),
                    curr_sum

                )
                
            return False,0,0,0

        solve(root)
        return ans[0]





            
        

        