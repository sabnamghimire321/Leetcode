class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')
     
        def down(node):
            nonlocal best
            if not node:
                return 0
            
            left = max(down(node.left), 0)
            right = max(down(node.right), 0)
            
            best = max(best, node.val + left + right)
            
            return node.val + max(left, right)
     
        down(root)
        return best
