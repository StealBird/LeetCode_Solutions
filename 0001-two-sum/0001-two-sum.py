class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i,num in enumerate(nums):
            if num not in hash:
                hash[num] = [i]
            else:
                hash[num].append(i)
        
        nums = sorted(nums)
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            sum = nums[left] + nums[right]
            
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                if nums[left] == nums[right]:
                    return [hash[nums[left]][0], hash[nums[right]][1]]
                else:
                    return [hash[nums[left]][0], hash[nums[right]][0]]
        return [-1,-1]
          