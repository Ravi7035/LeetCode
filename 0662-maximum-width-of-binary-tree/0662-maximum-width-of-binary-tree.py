# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q=deque([(root,0)])

        maximum_width=0
        while q:
            size=len(q)
            first_index=q[0][1]
            last_index=q[-1][1]
            maximum_width=max(maximum_width,last_index-first_index+1)

            for i in range(size):
                node,index=q.popleft()
            
                if node.left:
                    q.append((node.left,2*index))

                if node.right:
                    q.append((node.right,(2*index)+1))

        return maximum_width
                




        
        