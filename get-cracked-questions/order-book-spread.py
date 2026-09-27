# Given two lists of tuples, one is bids and one is asks
# Each tuple gives the price and size (price, size)
# Create a functiont that returns the:
# Mid price (best bid + best ask / 2)
# Bid-ask spread (best ask - best bid)
# Best bid is highest price in bid list
# Best ask is lowest price in ask list

def order_book_spread(bids: list[tuple[float, int]], asks: list[tuple[float, int]]) -> tuple[float, float]:
    # From bids find highest bid
    # From asks find lowest ask
    best_bid = 0
    for val in bids:
        if val[0] > best_bid:
            best_bid = val[0]
    
    best_ask = float("inf")
    for val in asks:
        if val[0] < best_ask:
            best_ask = val[0]

    # Compute mid
    mid = round(((best_bid + best_ask) / 2), 2)
    
    # Compute spread 
    spread = round((best_ask - best_bid), 2)

    # Return (mid, spread)
    return (mid, spread)

# Passed 