class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k >len(bloomDay):
            return -1

        def feasible(day:int) -> bool:
            bouquest = streak = 0
            for b in bloomDay:
                if b<=day:
                    streak += 1
                    if streak == k:
                        bouquest += 1
                        streak = 0
                else:
                    streak = 0
            return bouquest >= m

        low, high = min(bloomDay), max(bloomDay)
        while low<high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low
