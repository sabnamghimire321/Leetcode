class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)
                
            left_rob, left_skip = helper(node.left)
            right_rob, right_skip = helper(node.right)
            
            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_this, skip_this)
            
        return max(helper(root))
