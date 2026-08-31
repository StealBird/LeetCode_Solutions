class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0

        while(low<=high):
            result = 0
            mid = low+(high-low)//2

            for num in nums:
                result += (num+mid - 1)//mid
            
            if result <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
        