class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        result=0
        profit=0
        left=0
        for right in range(1,len(prices)):
            profit=prices[right]-prices[left]
            if profit<0:
                left=right
            result=max(result,profit)
        return result