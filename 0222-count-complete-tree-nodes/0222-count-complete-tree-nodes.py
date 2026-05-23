class Solution:

    def countNodes(self, root):

        if not root:
            return 0

        left_height = self.findLeftHeight(root)
        right_height = self.findRightHeight(root)

        # Perfect binary tree
        if left_height == right_height:

            return (2 ** left_height) - 1

        return (
            1
            + self.countNodes(root.left)
            + self.countNodes(root.right)
        )

    def findLeftHeight(self, node):

        height = 0

        while node:

            height += 1
            node = node.left

        return height

    def findRightHeight(self, node):

        height = 0

        while node:

            height += 1
            node = node.right

        return height