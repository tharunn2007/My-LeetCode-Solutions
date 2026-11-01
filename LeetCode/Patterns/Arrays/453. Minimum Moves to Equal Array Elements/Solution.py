class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxim = max(nums)
        count = 0 
        for i in range(len(nums)):
            if nums[i] == maxim:
                continue
            else:
                while nums[i]!=maxim:
                    nums[i]+=1
                    count+=1
        return count
            