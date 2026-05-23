# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """


        parent_nodes = {}

        q = deque([root])

        # Store parents
        while q:

            node = q.popleft()

            if node.val==start:
                start_node=node

            if node.left:

                parent_nodes[node.left] = node

                q.append(node.left)

            if node.right:

                parent_nodes[node.right] = node

                q.append(node.right)

        # BFS from target
        q = deque([start_node])

        visited = set([start_node])

        time=-1

        while q:
            size=len(q)

            for i in range(size):

                node = q.popleft()

                neighbours = [
                    node.left,
                    node.right,
                    parent_nodes.get(node)
                ]

                for nei in neighbours:

                    if nei and nei not in visited:

                        visited.add(nei)

                        q.append(nei)

            time+=1

        return time
        