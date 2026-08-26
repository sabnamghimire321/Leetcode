class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0
        NOT_COVERED, COVERED, HAS_CAMERA = 0, 1, 2
        
        def dfs(node):
            nonlocal cameras
            if not node:
                return COVERED
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == NOT_COVERED or right == NOT_COVERED:
                cameras += 1
                return HAS_CAMERA
            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED
            return NOT_COVERED
            
        if dfs(root) == NOT_COVERED:
            cameras += 1
            
        return cameras
