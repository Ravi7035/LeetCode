class Solution(object):
    def flatten(self, root):

        prev = [None]

        def solve(node):

            if not node:
                return

            left = node.left
            right = node.right

            if prev[0]:
                prev[0].right = node
                prev[0].left = None

            prev[0] = node

            solve(left)
            solve(right)

        solve(root)