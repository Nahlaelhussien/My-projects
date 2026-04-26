class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((intervals[i][0], i) for i in range(n))
        result = []
        for start, end in intervals:
            idx = bisect.bisect_left(starts, (end,))
            if idx < n:
                result.append(starts[idx][1])
            else:
                result.append(-1)
        
        return result
