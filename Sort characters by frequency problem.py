from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        sorted_count=sorted(count.items(), key=lambda x: x[1], reverse=True)
        result=[]
        for char,freq  in sorted_count:
            result.append(char * freq)
        return "".join(result)
