import random
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        result=0
        n = len(piles) // 3
        for i in range(1,2*n,2):
            result+=piles[i]
        return result

