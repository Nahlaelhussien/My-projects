class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        left = 0
        best = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] >= n:
                left += 1
            best = max(best, right - left + 1)
        return n - best
