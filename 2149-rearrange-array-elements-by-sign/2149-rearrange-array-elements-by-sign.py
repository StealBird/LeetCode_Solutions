class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        k = len(nums)
        ans = [0]*k
        pos_Ind = 0
        neg_Ind = 1

        for i in range(k):
            if nums[i]>0:
                ans[pos_Ind] = nums[i]
                pos_Ind += 2
            else:
                ans[neg_Ind] = nums[i]
                neg_Ind += 2
        return ans
        