# Kelly fraction is used for optimal bet sizing given chance of winning and return
# Given two floats (p, b)
# p: probability of winning
# b: net odds 
# If b = 2.0, that means a bet of $10 returns $20, 2x the stake
# Create a function using the kelly criterion formula that returns:
# The optimal bet sizing (fraction of bankroll that maximizes long-run return)
# If the optimal bet sizing is negative return 0.0, don't bet/trade


def kelly_fraction(p, b):
    # Your code here
    kelly_fraction = (p - ((1 - p) / b))
    if kelly_fraction < 0:
        return 0.0
    return round(kelly_fraction, 4)