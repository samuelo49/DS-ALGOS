"""
Given an array of floats that represents the movement in the share
price of a company over time,
 design an algorithm that determines the maximum profit that could
have been made by buying and
 then selling a single share over the time period.
The buy must occur before the sell.
[7,1,5,3,6,4]
"""


def maxProfitPotential(prices):
    maxProfit = 0
    minPrice = float("inf")

    for currentPrice in prices:
        profit = currentPrice - minPrice
        minPrice = min(minPrice,currentPrice)
        maxProfit = max(maxProfit,profit)       
    return maxProfit

print(maxProfitPotential([7,1,5,3,6,4]))



