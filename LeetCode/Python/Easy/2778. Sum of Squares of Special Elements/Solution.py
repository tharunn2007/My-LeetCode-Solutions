class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Loop through the list using 1-based indexing
        for i in range(1, n + 1):
            # Check if i divides the length of the array perfectly
            if n % i == 0:
                # nums is 0-indexed, so index i corresponds to nums[i - 1]
                element = nums[i - 1]
                total_sum += element * element
                
        return total_sum