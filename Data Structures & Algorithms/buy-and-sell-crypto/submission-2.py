class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0
        for i in prices :
            if i < min_profit:
                min_profit = i
            if i - min_profit > max_profit:
                max_profit = i - min_profit

        return max_profit 



 


        