class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def piecesNeeded(maxSum: int) -> int:
            pieces = 1
            curr = 0
            for num in nums:
                if curr + num > maxSum:
                    pieces += 1
                    curr = num
                else:
                    curr += num
            return pieces

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if piecesNeeded(mid) <= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
        