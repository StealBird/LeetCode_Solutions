class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)


        counter = 1
        if n == 1: return True
        for i in range(1, 2 * n):
            if nums[(i-1) % n] <= nums[i%n]:
                counter += 1
            else:
                counter = 1
            
            if counter == n:
                return True
        return False