# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val > curr.val:
                # If there's no right child, insert here
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                # If there's no left child, insert here
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
                
        return root

        

            
                

                



        