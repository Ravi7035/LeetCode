# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def solve(left,right,nums):
            if left > right:
                return None

            mid=(left+right)//2

            root=TreeNode(nums[mid])
            root.left=solve(left,mid-1,nums)
            root.right=solve(mid+1,right,nums)

            return root

        return solve(0,len(nums)-1,nums)

