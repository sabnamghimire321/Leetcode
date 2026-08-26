class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
     
        def height(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
                
            left = height(node.left)
            right = height(node.right)
            
            best = max(best, left + right)
            return 1 + max(left, right)
     
        height(root)
        return best
