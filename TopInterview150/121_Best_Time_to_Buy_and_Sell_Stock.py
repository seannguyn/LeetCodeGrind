# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            current_profit = prices[i] - min_price
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit

if __name__ == "__main__":
    solution = Solution()
