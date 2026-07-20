class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_Pro = 0
        min_Price = float("+inf")

        for i in range(0,n):
            if prices[i] < min_Price:
                min_Price = prices[i]
            if prices[i] > max_Pro:
                max_Pro = max(max_Pro,prices[i]-min_Price)
        return max_Pro
        