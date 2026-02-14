class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={}
        for i in range(len(indices)):
            dic[indices[i]]=s[i]
        sorted_indices=sorted(indices)
        result=""
        for key in sorted_indices:
            result=result+dic[key]
        return result
