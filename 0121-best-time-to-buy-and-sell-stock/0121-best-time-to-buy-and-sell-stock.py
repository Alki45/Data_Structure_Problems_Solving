class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = float ('inf')
        
        max_profit = 0

        for price in prices:
            if price <= min_num:
                min_num = price
            else:
                max_profit = max(max_profit,price - min_num)
        return max_profit
        