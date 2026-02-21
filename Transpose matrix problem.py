class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=list(map(list, zip(*matrix)))   
        return result
