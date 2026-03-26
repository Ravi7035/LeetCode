# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):

        stack1=[root]
        stack2=[]

        if not root:
            return []

        while stack1:
            
            node=stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        result=[]
        while stack2:
            result.append(stack2.pop().val)

        return result


       