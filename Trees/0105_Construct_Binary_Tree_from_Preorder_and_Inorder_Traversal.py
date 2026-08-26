class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        preorder_pos = 0
     
        def helper(in_left, in_right):
            nonlocal preorder_pos
            if in_left > in_right:
                return None
                
            root_val = preorder[preorder_pos]
            preorder_pos += 1
            
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
     
        return helper(0, len(inorder) - 1)
