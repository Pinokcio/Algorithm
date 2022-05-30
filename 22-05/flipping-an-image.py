class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[k^1 for k in i[::-1]] for i in image]
        
