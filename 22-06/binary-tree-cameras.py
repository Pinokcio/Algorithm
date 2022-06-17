# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def solve(node): #return 사용한 카메라 수, 현재 노드가 커버됐는지 여부, 현재 노드에서 카메라를 사용했는지 여부
            if not node:
                return 0, 1, 0
            l = solve(node.left)
            r = solve(node.right)
            print(l ,r)
            cam = l[0] + r[0]
            if not (l[1] == 1 and r[1] == 1): #하위 노드가 커버 안된 경우 현재 노드에서 커버해주기 위함
                cam += 1
                return cam, 1, 1
            else: #하위 노드가 모두 커버됐으므로, 하위 노드가 현재 노드를 커버해줄 수 있는지 확인
                if l[2] == 1 or r[2] == 1: #커버 가능한 경우
                    return cam, 1, 0
                else:
                    return cam, 0, 0
        cur = solve(root)
        print(cur)
        if cur[1] == 0:
            return cur[0] + 1
        return cur[0]
            
            
            
            
#상위노드와 하위노드를 살펴야함
"""
모든 노드에서 현재노드와 하위노드를 살펴본다고 생각하면 상위노드를 굳이 볼 필요는 없음
(상위노드에서 현재노드는 하위노드이기 때문)
확실한 것은 재귀를 이용하여 노드의 끝부터 체크한다고 했을 때 하위노드는 꼭 cover 돼있어야 한다. 
왜냐하면 현재노드의 부모노드가 현재노드는 cover할 수 있지만 현재노드의 하위 노드는 cover할 수 없기때문이다.
고로 다음과 같은 경우의수
1. 하위 노드만 covered 현재 노드 not covered
2. 현재 노드 하위 노드 모두 covered - 현재 노드 카메라 x
3. 현재 노드 하위 노드 모두 covered - 현재 노드 카메라 o
위 경우의 수를 확인하기 위해 현재 노드와 하위 노드를 확인해야한다.
"""
