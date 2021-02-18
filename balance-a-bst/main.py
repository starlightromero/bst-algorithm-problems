class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        self.inOrderTraversal(root, nodes)
        n = len(nodes)
        return self.constructBST(nodes, 0, n - 1)

    def inOrderTraversal(self, node, nodes):
        if node.left:
            self.inOrderTraversal(node.left, nodes)
        nodes.append(node)
        if node.right:
            self.inOrderTraversal(node.right, nodes)

    def constructBST(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self.constructBST(nodes, start, mid - 1)
        node.right = self.constructBST(nodes, mid + 1, end)
        return node
