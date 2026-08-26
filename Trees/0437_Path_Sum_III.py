from collections import defaultdict
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0
     
        def dfs(node, running_sum):
            nonlocal result
            if not node:
                return
            running_sum += node.val
            result += prefix_count[running_sum - targetSum]
            prefix_count[running_sum] += 1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            prefix_count[running_sum] -= 1
     
        dfs(root, 0)
        return result
