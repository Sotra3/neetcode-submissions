class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        buy:int=prices[0]
        profit:int=0
        for i in prices:
            profit=max(profit,i-buy)
            buy=min(i,buy)
        return profit

        