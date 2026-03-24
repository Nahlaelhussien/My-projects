class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if  m==0:
            nums1[0:]=nums2
        elif n==0:
            nums1=nums1
        else: 
            nums1[m:]=nums2
            list.sort(nums1)
