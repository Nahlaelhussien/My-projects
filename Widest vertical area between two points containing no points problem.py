class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [p[0] for p in points]
        xs.sort()
        ans = 0
        for i in range(1, len(xs)):
            ans = max(ans, xs[i] - xs[i - 1])
        return ans
