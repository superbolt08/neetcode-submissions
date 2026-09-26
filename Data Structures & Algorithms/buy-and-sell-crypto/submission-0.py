class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if(price < min_price):
                min_price = price
            elif((price - min_price) > max_profit):
                max_profit = price - min_price
        return max_profit


# sort the array
# place a pointer on min and max value
# if min index < max index
    # then return max index - min index
# else max index -=1
# keep going until max index = min index