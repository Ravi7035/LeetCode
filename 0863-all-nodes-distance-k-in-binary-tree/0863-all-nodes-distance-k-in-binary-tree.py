from collections import deque

class Solution:
    def distanceK(self, root, target, k):

        parent_nodes = {}

        q = deque([root])

        # Store parents
        while q:

            node = q.popleft()

            if node.left:

                parent_nodes[node.left] = node

                q.append(node.left)

            if node.right:

                parent_nodes[node.right] = node

                q.append(node.right)

        # BFS from target
        q = deque([(target, 0)])

        visited = set([target])

        ans = []

        while q:

            node, dist = q.popleft()

            if dist == k:

                ans.append(node.val)

            if dist > k:
                break

            neighbours = [
                node.left,
                node.right,
                parent_nodes.get(node)
            ]

            for nei in neighbours:

                if nei and nei not in visited:

                    visited.add(nei)

                    q.append((nei, dist + 1))

        return ans