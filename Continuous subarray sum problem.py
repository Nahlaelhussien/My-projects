class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            r = total % k
            if r in seen:
                if i - seen[r] >= 2:
                    return True
            else:
                seen[r] = i
        return False



