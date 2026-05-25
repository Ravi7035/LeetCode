# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q=deque([root])
        encoded_string=[]
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                
                if node:
                    encoded_string.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)

                else:
                    encoded_string.append("#")
               
        return ",".join(encoded_string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data=data.split(",")

        root=TreeNode(data[0])

        q=deque([root])
        i=1
        while q and i < len(data):
            node=q.popleft()

            if data[i]!="#":
                node.left=TreeNode(int(data[i]))
                q.append(node.left)

            i+=1

            if data[i]!="#":
                node.right=TreeNode(int(data[i]))
                q.append(node.right)

            i+=1

        return root




        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))