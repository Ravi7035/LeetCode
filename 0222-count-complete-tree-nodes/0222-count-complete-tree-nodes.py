# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        node_sum=[0]
        def solve(root):

            if not root:
                return

            node_sum[0]+=1

            solve(root.left)
            solve(root.right)

        solve(root)
        return node_sum[0]


        