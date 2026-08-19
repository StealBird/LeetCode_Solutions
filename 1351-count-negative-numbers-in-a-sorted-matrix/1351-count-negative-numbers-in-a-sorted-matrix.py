class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for row in grid:
            low = 0
            high = n

            while low < high:
                mid = (low + high) // 2
                if row[mid] < 0:
                    high = mid

                else:
                    low = mid + 1
            count += n - low
        return count

        