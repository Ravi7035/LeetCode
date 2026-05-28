# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def path(node,descendant,temp):

            if not node:
                return

            temp.append(node)

            if node.val==descendant.val:
                return temp[:]

            if node.val > descendant.val:

                left=path(node.left,descendant,temp)

                if left:
                    return left
            else:

                right=path(node.right,descendant,temp)

                if right:
                    return right

            temp.pop()

        first_descendant=path(root,p,[])
        second_descendant=path(root,q,[])

        second_descendant=set(second_descendant)

        for i in range(len(first_descendant)-1,-1,-1):

            if first_descendant[i]  in second_descendant:

                return first_descendant[i]


        

        
        