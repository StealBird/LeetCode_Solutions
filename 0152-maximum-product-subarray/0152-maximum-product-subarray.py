class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_Prod = min_Prod = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_Prod, min_Prod = min_Prod, max_Prod

            max_Prod = max(num, num*max_Prod)
            min_Prod = min(num, num*min_Prod)

            res = max(res,max_Prod)
        return res
    