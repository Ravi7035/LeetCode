# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        output=[0]

        def solve(root,current_max):

            if not root:
                return 

            if root.val >= current_max:
                output[0]+=1
                current_max=root.val
            
            solve(root.left,current_max)
            solve(root.right,current_max)

        solve(root,float('-inf'))


        return output[0]

        

    

            
        
        
        