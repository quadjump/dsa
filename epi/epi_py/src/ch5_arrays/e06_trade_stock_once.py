### 5.6 Buy and sell a stock once ###

"""
This problem is concerned with the problem of optimally buying and selling a stock once,
as described on Page 2.

As an example, consider the following sequence of stock prices:
(310,315,275,295,260,270,290,230,255,250). The maximum profit that can be made with one buy
and one sell is 30—buy at 260 and sell at 290. Note that 260 is not the lowest price, nor 290 the
highest price.

Write a program that takes an array denoting the daily stock price, and returns the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.

> From Page 2:
> Let's begin with Figure 1 below. It depicts movements in the share price of a company over 40 days.
Specifically, for each day, the chart shows the daily high and low, and the price at the opening bell
(denoted by the white square). Suppose you were asked in an interview to design an algorithm
that determines the maximum profit that could have been made by buying and then selling a single
share over a given day range, subject to the constraint that the buy and the sell have to take place
at the start of the day. (This algorithm may be needed to backtest a trading strategy.)
"""
import sys
from typing import List, NewType, Tuple


Buy = NewType('Buy', int)
Sell = NewType('Sell', int)

def grift(daily_prices: List[int]) -> int:
    """
    # >>> grift([310,315,275,295,260,270,290,230,255,250])
    # 30
    #
    """
    curr_min, max_profit = sys.maxsize, 0
    
    for price in daily_prices:
        today_profit = price - curr_min
        max_profit = max(max_profit, today_profit)
        curr_min = min(curr_min, price)
        
    return max_profit


def grift_(daily_prices: List[int]) -> Tuple[Buy, Sell]:
    """
    # >>> grift_([310,315,275,295,260,270,290,230,255,250])
    # >>> 
    # (230, 315)
    #
    """

    match daily_prices:
        # case []: return None
        case [x]: return Buy(x), Sell(x)
        case [x,y]: return Buy(x), Sell(x)
        case _: return Buy(0), Sell(0)

    # min, max = Buy(daily_prices[0]), Sell(daily_prices[0])

    # for p in daily_prices:
    #     if p < min:
    #         min = Buy(p)
    #     elif p > max:
    #         max = Sell(p)

    # return min, max