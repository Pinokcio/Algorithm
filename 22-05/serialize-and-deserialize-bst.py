# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(root):
            if root is None:
                res.append('null')
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "/".join(res)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        from collections import deque
        q = deque(data.split('/'))
        def dfs():
            n = q.popleft()
            if n == 'null':
                return None
            tmp = TreeNode(n)
            tmp.left = dfs()
            tmp.right = dfs()
            return tmp
            
        return dfs()
    
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
