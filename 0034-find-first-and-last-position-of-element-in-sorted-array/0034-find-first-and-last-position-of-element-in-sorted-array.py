class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n-1

        def firstIndex(nums, target):
            first = -1
            start = 0
            end = n-1

            while(start <= end):
                mid = (start + end )//2
                if nums[mid] == target:
                    first = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    end = mid - 1
            return first

        def lastIndex(nums, target):
            last = -1
            start = 0
            end = n-1
            while (start <= end):
                mid = (start + end)//2

                if nums[mid] == target:
                    last = mid
                    start = mid+1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last
            
        first = firstIndex(nums,target)
        last = lastIndex(nums,target)
        return [first,last]      