class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        max_area=0
        stk.append(0)
        heights.append(0)
        for i, cur_height in enumerate(heights):
            while stk and heights[stk[-1]] > cur_height:
                local_max_height = heights[stk.pop()]
                width = 0
                if not stk:
                    width = i
                else:
                    width = i - stk[-1] - 1
                max_area = max(max_area, local_max_height * width)
            stk.append(i)
        return max_area
