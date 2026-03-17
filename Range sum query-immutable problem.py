class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.prefix=[0] * (n+1)
        self.prefix[0]=nums[0]
        for i in range(n):
            self.prefix[i+1]=self.prefix[i]+nums[i]
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
    
