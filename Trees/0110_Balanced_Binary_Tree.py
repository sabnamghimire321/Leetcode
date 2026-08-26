class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            left = check(node.left)
            if left == -1:
                return -1
                
            right = check(node.right)
            if right == -1:
                return -1
                
            if abs(left - right) > 1:
                return -1
                
            return 1 + max(left, right)
     
        return check(root) != -1
