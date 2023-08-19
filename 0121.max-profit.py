def max_profit(prices):
    """
    Finds the maximum achievable profit from buying a stock on one day and
    selling it at a different date
    Inputs:
        prices (list of ints): array to represent prices
    Returns: maximum_profit (int): the max profit
    """
    maximum_profit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[right] - prices[left] <= 0:
            left = right
        else:
            current_profit = prices[right] - prices[left]
            maximum_profit = max(maximum_profit, current_profit)
        right += 1
        
    return max_profit