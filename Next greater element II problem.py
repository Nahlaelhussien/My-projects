class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] *n
        stack = []
        for i in range(n*2):
            while stack and nums[stack[-1]] <nums[i%n]:
                indx= stack.pop()
                result[indx] = nums[i%n]
            if i < n:
                stack.append(i)
        return result
