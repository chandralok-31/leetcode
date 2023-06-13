class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        sump=0
        while r<len(prices):
            if prices[r]>prices[l]:
                sump+=prices[r]-prices[l]
                l=r
                
            else:
                l=r
            r+=1
        return sump
        