# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        stack=[]
        def solve(root,stack):
            if not root:
                return 
            solve(root.left,stack)
            stack.append(root.val)
            solve(root.right,stack)

        solve(root,stack)

        i=0
        j=len(stack)-1
        
        while i < j:
            if stack[i]+stack[j]==k:
                return True

            elif stack[i]+stack[j] < k:
                i+=1
            else:
                j-=1

        return False

            
        