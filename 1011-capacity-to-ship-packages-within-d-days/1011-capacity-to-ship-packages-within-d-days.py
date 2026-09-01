class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(capacity: int) -> int:
            days_count = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    days_count += 1
                    current_load = 0
                current_load += w
            return days_count

        low, high = max(weights) , sum(weights)

        while (low < high):
            mid = (low + high ) // 2

            if days_needed(mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low
        