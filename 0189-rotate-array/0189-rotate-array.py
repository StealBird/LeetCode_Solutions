class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        start = 0
        end = n-1
        if n == 0 or k == 0:
            return nums
        def reverse(nums,start,end):
            while start < end:
               nums[start],nums[end]=nums[end],nums[start]
               start += 1
               end -= 1

        
        reverse(nums,start,end)
        reverse(nums,start,k-1)
        reverse(nums,k,end)

        return nums
    
   