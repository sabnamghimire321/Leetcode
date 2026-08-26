class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left_spine(root)

    def _push_left_spine(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left_spine(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
