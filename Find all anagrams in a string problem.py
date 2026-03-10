class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_sorted = sorted(p)
        result=[]
        for i in range(len(s) - len(p) + 1):
            if sorted(s[i:i+len(p)]) == p_sorted:
                result.append(i)
        return result
