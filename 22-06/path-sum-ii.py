# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root is None:
            return []
        def getsum(node, sumn, his):
            tmp = his[:]
            tmp.append(node.val)
            sumn += node.val
            if node.left is None and node.right is None and sumn == targetSum:
                ans.append(tmp)
            if node.left is not None:
                getsum(node.left, sumn, tmp)
            if node.right is not None:
                getsum(node.right, sumn, tmp)
        getsum(root, 0, [])
        return ans
