class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = [None]
        middle = [None]
        last = [None]
        prev = [None]
        self.trackNodesToSwap(root, first, middle, last, prev)
        if first[0] and last[0]:
            first[0].val, last[0].val = (last[0].val, first[0].val)
        elif first[0] and middle[0]:
            first[0].val, middle[0].val = middle[0].val, first[0].val

    def trackNodesToSwap(self, root, first, middle, last, prev):
        if root:
            self.trackNodesToSwap(root.left, first, middle, last, prev)
            if prev[0] and root.val < prev[0].val:
                if not first[0]:
                    first[0] = prev[0]
                    middle[0] = root
                else:
                    last[0] = root
            prev[0] = root
            self.trackNodesToSwap(root.right, first, middle, last, prev)
