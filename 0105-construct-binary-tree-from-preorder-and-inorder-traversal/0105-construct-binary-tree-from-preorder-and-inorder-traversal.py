# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map={}
        #building inorder map at first

        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i

        pre_index=[0]

        def helper(left,right):

            if left > right:
                return None

            root_val=preorder[pre_index[0]]

            pre_index[0]+=1

            root=TreeNode(root_val)

            mid=inorder_map[root_val]

            root.left=helper(left,mid-1)

            root.right=helper(mid+1,right)

            return root

        return helper(0,len(inorder)-1)
