class Solution:
    def smallestNumber(self, num: int) -> int:
        result=0
        l = list(str(abs(num)))
        if num < 0:
            l.sort(reverse=True)
        else:
            l.sort()
            if l[0]=='0':
                for i in range(1, len(l)):
                    if l[i] != '0':
                        l[0], l[i] = l[i], l[0]
                        break
        return int("".join(l)) * (-1 if num < 0 else 1)
        
