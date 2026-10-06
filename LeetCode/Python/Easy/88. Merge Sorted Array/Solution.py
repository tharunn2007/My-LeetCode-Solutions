class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = len(nums1)-len(nums2)

        n = len(nums2)

        x = len(nums1) # also equal to nums1+nums2