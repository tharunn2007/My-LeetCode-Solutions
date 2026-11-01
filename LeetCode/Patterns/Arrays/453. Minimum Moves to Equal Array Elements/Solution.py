class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxim = max(nums)
        count = 0 
        for i in range(len(nums)):
            if nums[i] == maxim:
                continue
            else:
                	[-1000000000, 10000