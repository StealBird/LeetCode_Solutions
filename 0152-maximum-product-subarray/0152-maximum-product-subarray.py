class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxSoFar = nums[0]
        curMax = nums[0]
        curMin = nums[0]
        
        for i in range(1,n):
            if nums[i] < 0:
                curMax,curMin = curMin,curMax
            
            curMax = max(nums[i], curMax*nums[i])
            curMin = min(nums[i], curMin*nums[i])

            maxSoFar = max(maxSoFar,curMax)
        
        return maxSoFar
        