class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = len(nums)
        curr_Sum = nums[0]
        max_Sum = nums[0]

        for i in range(1 , m):
            curr_Sum = max(nums[i],curr_Sum+nums[i])
            max_Sum = max(max_Sum, curr_Sum)
        return max_Sum
        