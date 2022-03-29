# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if node is not None:
                # 왼쪽 탐색
                dfs(node.left)
                result.append(node.val)
                # 오른쪽 탐색
                dfs(node.right)
        
        dfs(root)
        
        return result
