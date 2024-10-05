from typing import List


class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1

        while (sell < len(prices)):
            seen_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(seen_profit, max_profit)
            else:
                buy = sell
            sell += 1

        return max_profit


result = Solution()
prices = [7, 1, 5, 3, 6, 4]  # output = 5
print(result.maxProfit(prices))
