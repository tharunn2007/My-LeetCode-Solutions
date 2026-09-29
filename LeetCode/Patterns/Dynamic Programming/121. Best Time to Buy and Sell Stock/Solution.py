class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prices = prices[0]

        max_profit = 0

        for i in prices:
            if i<min_prices:
                min_prices = i
            elif i-min_prices>max_profit:
                max_profit = i-min_prices
        return max_profit


            


                

                




            


        

        



        