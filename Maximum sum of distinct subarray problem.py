class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result=0
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            if len(set(window)) == k:
                result = max(result, sum(window))
        return result
