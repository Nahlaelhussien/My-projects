class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        result=0
        for i in range(len(s)):
            while s[i] in sub:
                sub = sub[1:]   
            
            sub += s[i]
            result = max(result, len(sub))
        
        return result
