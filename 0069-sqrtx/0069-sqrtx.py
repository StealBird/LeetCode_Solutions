class Solution:
    def exactSqrt(self, x: int) -> int:
        low = 0
        high = x//2
        if x == 1:
            return 1

        while(low<=high):
            mid = (low+high) // 2

            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return None

    def closestSqrt(self, x: int) -> int:
        low, high = 0, x//2
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:         
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans 

    def mySqrt (self, x:int) -> int:
        res = self.exactSqrt(x)
        if res is not None:
            return res
        return self.closestSqrt(x)

        