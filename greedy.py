
#brute force
def brute_force_get_max_profit(stock_prices):
    max_till_now = 0

    for l in range(len(stock_prices)):
        for r in range(l+1, len(stock_prices)):

            if stock_prices[r] - stock_prices[l] > max_till_now:
                max_till_now = stock_prices[r] - stock_prices[l]
    
    return max_till_now

def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError("Getting a profit requires at least 2 prices")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices:
        min_price = min(min_price, price)

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit
    
    return max_profit


if __name__ == '__main__':
    stock_prices = [10, 7, 5, 8, 11, 9]
    
    print(get_max_profit(stock_prices))