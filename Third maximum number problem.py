class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        print(nums)
        if len(nums)<=2:
            return nums[0]
        else:
            return nums[2]
