class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #greedy to maximise the profit
        maxprofit = 0

        #instead of finidng glabal minimum we find minimum with max profit yeild
        minprice = prices[0]

        for i in prices:
            if i<minprice:
                minprice = i

            elif i-minprice > maxprofit:
                maxprofit = i-minprice
        return maxprofit

