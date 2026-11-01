class Solution:
    def minMoves(self, nums: list[int]) -> int:
        #number additions to give max  = number of subtraction to give min so yeaa easy shi
        minim = min(nums)
        count = 0

        for i in range(len(nums)):
            count += nums[i] - minim

        return count