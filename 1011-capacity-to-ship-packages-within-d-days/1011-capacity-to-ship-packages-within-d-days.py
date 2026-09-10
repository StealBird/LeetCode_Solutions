class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2

            # inlined "days needed for this capacity" check
            days_count = 1
            current_load = 0
            for w in weights:
                if current_load + w > mid:
                    days_count += 1
                    current_load = 0
                current_load += w

            if days_count <= days:
                high = mid
            else:
                low = mid + 1

        return low