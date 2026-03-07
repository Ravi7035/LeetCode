# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        output=[]
        def PostOrder(node):
            if node is None:
                return 
            PostOrder(node.left)
            PostOrder(node.right)
            output.append(node.val)
        PostOrder(root)
        return output