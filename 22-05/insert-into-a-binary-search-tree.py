# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertnode(cur, n):
            if n < cur.val:
                if cur.left:
                    insertnode(cur.left, n)
                else:
                    cur.left = TreeNode(n)
            else:
                if cur.right:
                    insertnode(cur.right, n)
                else:
                    cur.right = TreeNode(n)
        if root is None:
            root = TreeNode(val)
        else:
            insertnode(root, val)
        return root
#########################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
