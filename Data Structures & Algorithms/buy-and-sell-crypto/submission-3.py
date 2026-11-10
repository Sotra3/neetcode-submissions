class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        buy:int=prices[0]
        profit:int=0
        for price in prices:
            profit=max(profit,price-buy)
            buy=min(price,buy)
        return profit

        